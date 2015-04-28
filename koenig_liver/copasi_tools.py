"""
Simulation wrapper for COPASI. 
The latest copasi bindings were installed.

python-copasi

Created on Tue Apr 28 16:35:37 2015
@author: mkoenig
"""

from COPASI import *
import time
import sys

def simulate(filename, t0, duration, steps, absTol, relTol, write_report=False):
    '''
    Simulate SBML with given tolerances.
    Adapted from simulation example from COPASI python API.
    
    # Begin CVS Header 
    #   $Source: /Volumes/Home/Users/shoops/cvs/copasi_dev/copasi/bindings/python/examples/example3.py,v $ 
    #   $Revision: 1.7 $ 
    #   $Name:  $ 
    #   $Author: shoops $ 
    #   $Date: 2012/03/05 18:09:32 $ 
    # End CVS Header 

    # Copyright (C) 2011 by Pedro Mendes, Virginia Tech Intellectual 
    # Properties, Inc., University of Heidelberg, and The University 
    # of Manchester. 
    # All rights reserved. 
    '''    
        
    assert CCopasiRootContainer.getRoot() != None
    # create a datamodel
    dataModel = CCopasiRootContainer.addDatamodel()
    # assert CCopasiRootContainer.getDatamodelList().size() == 1
    try:
        # load the model
        time_start = time.time()
        print "Load model {} ...".format(filename)
        dataModel.importSBML(filename)
        loadTime = time.time()-time_start
        print "Load time: {}".format(loadTime)
    except:
        print >> sys.stderr,  "Error while importing the model from file named \"" + filename + "\"." 
        return 1
    model = dataModel.getModel()
    assert model != None
    
    if (write_report):
        # create a report with the correct filename and all the species against
        # time.
        print "Create report ..."   
        reports = dataModel.getReportDefinitionList()
        # create a report definition object
        report = reports.createReportDefinition("Report", "Output for timecourse")
        # set the task type for the report definition to timecourse
        report.setTaskType(CCopasiTask.timeCourse)
        # we don't want a table
        report.setIsTable(False)
        # the entries in the output should be seperated by a ", "
        report.setSeparator(CCopasiReportSeparator(", "))

        # we need a handle to the header and the body
        # the header will display the ids of the metabolites and "time" for
        # the first column
        # the body will contain the actual timecourse data
        header = report.getHeaderAddr()
        body = report.getBodyAddr()
    
        body.push_back(CRegisteredObjectName(CCopasiObjectName(dataModel.getModel().getCN().getString() + ",Reference=Time").getString()))
        body.push_back(CRegisteredObjectName(report.getSeparator().getCN().getString()))
        header.push_back(CRegisteredObjectName(CCopasiStaticString("time").getCN().getString()))
        header.push_back(CRegisteredObjectName(report.getSeparator().getCN().getString()))

        iMax = model.getMetabolites().size()
        for i in range(0,iMax):
            metab = model.getMetabolite(i)
            assert metab != None
            # we don't want output for FIXED metabolites right now
            if (metab.getStatus() != CModelEntity.FIXED):
                # we want the concentration oin the output
                # alternatively, we could use "Reference=Amount" to get the
                # particle number
                body.push_back(CRegisteredObjectName(metab.getObject(CCopasiObjectName("Reference=Concentration")).getCN().getString()))
                # add the corresponding id to the header
                header.push_back(CRegisteredObjectName(CCopasiStaticString(metab.getSBMLId()).getCN().getString()))
                # after each entry, we need a seperator
                if(i!=iMax-1):
                    body.push_back(CRegisteredObjectName(report.getSeparator().getCN().getString()))
                    header.push_back(CRegisteredObjectName(report.getSeparator().getCN().getString()))
    

    # get the trajectory task object
    print "Trajectory task ..."
    trajectoryTask = dataModel.getTask("Time-Course")
    # if there isn't one
    if (trajectoryTask == None):
        # create a one
        trajectoryTask = CTrajectoryTask()
        # add the time course task to the task list
        # this method makes sure the object is now owned by the list
        # and that SWIG does not delete it
        dataModel.getTaskList().addAndOwn(trajectoryTask)

    # run a deterministic time course
    trajectoryTask.setMethodType(CCopasiMethod.deterministic)

    # pass a pointer of the model to the problem
    trajectoryTask.getProblem().setModel(dataModel.getModel())

    # actiavate the task so that it will be run when the model is saved
    # and passed to CopasiSE
    trajectoryTask.setScheduled(True)


    if (write_report):
        # do not write report for fair comparison, only interested in the 
        # actual integration time    
        # set the report for the task
        trajectoryTask.getReport().setReportDefinition(report)
        # set the output filename
        trajectoryTask.getReport().setTarget("test_report.txt")
        # don't append output if the file exists, but overwrite the file
        trajectoryTask.getReport().setAppend(False)

    # get the problem for the task to set some parameters
    problem = trajectoryTask.getProblem()
    # steps
    problem.setStepNumber(steps)
    # start time of simulation
    dataModel.getModel().setInitialTime(t0)
    # end time of simulation
    problem.setDuration(duration)
    # tell the problem to actually generate time series data
    problem.setTimeSeriesRequested(True)

    # set some parameters for the LSODA method through the method
    method = trajectoryTask.getMethod()

    parameter = method.getParameter("Absolute Tolerance")
    assert parameter != None
    assert parameter.getType() == CCopasiParameter.UDOUBLE
    parameter.setValue(absTol)

    parameter = method.getParameter("Relative Tolerance")
    assert parameter != None
    assert parameter.getType() == CCopasiParameter.UDOUBLE
    parameter.setValue(relTol)
    
    parameter = method.getParameter("Max Internal Steps")
    assert parameter != None
    assert parameter.getType() == CCopasiParameter.UINT
    parameter.setValue(50000)

    result=True
    
    try:
        # now we run the actual trajectory 
        print "Run simulation ..."
        startTime = time.time()
        result = trajectoryTask.process(True)
        endTime = time.time()
        print "Simulation time: {}".format(endTime-startTime)    
    except:
        print >> sys.stderr,  "Error. Running the time course simulation failed." 
        # check if there are additional error messages
        if CCopasiMessage.size() > 0:
            # print the messages in chronological order
            print >> sys.stderr, CCopasiMessage.getAllMessageText(True)
        return 1
    
    if result == False:
        print >> sys.stderr,  "Error. Running the time course simulation failed." 
        # check if there are additional error messages
        if CCopasiMessage.size() > 0:
            # print the messages in chronological order
            print >> sys.stderr, CCopasiMessage.getAllMessageText(True)
        return 1

    # get access to the timeseries
    timeseries = trajectoryTask.getTimeSeries()
    return {'startTime': startTime, 'endTime': endTime, 'timeseries': timeseries}
    # return [startTime, endTime, endTime-startTime, loadTime]