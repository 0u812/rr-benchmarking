from roadrunner import *
import time
import csv
import sys

tests = [ \
('00001',   "./00001/00001-sbml-l2v4.xml"),
('00002',   "./00002/00002-sbml-l2v4.xml"),
('00050',  "./00050/00050-sbml-l2v4.xml"),
('00100', "./00100/00100-sbml-l2v4.xml"),
('00150', "./00150/00150-sbml-l2v4.xml"),
('00200', "./00200/00200-sbml-l2v4.xml"),
('00250', "./00250/00250-sbml-l2v4.xml"),
('00300', "./00300/00300-sbml-l2v4.xml"),
('00350', "./00350/00350-sbml-l2v4.xml"),
('00400', "./00400/00400-sbml-l2v4.xml"),
('00450', "./00450/00450-sbml-l2v4.xml"),
('00500' "./00500/00500-sbml-l2v4.xml")]

start = 0;
end = 50;
steps = 50;

csvwriter = csv.writer(sys.stdout, delimeter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def timeit(d, fname):
    startTime = time.time()
    r=RoadRunner(fname)
    loadTime = time.time()
    m=r.simulate(start,end,steps)
    endTime = time.time()

    csvwriter.writerow([d, loadTime-startTime, endTime-loadTime, endTime-startTime])


for n in range(3):
  csvwriter.writerow(['Trial {}'.format(n+1)])
  csvwriter.writerow(['Num', 'Load_time', 'Run_time', 'Total_time'])
  for t in tests:
      timeit(*t)

