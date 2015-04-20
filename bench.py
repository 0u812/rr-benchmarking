from roadrunner import *
import time


tests = [ \
(1,   "./00001/00001-sbml-l3v1.xml"),
(2,   "./00002/00002-sbml-l3v1.xml"),
(50,  "./00050/00050-sbml-l3v1.xml"),
(100, "./00100/00100-sbml-l3v1.xml"),
(150, "./00150/00150-sbml-l3v1.xml"),
(200, "./00200/00200-sbml-l3v1.xml"),
(250, "./00250/00250-sbml-l3v1.xml"),
(300, "./00300/00300-sbml-l3v1.xml"),
(350, "./00350/00350-sbml-l3v1.xml"),
(400, "./00400/00400-sbml-l3v1.xml"),
(450, "./00450/00450-sbml-l3v1.xml"),
(500, "./00500/00500-sbml-l3v1.xml")]

start = 0;
end = 50;
steps = 50;


def timeit(num, fname):
    startTime = time.time()
    r=RoadRunner(fname)
    loadTime = time.time()
    m=r.simulate(start,end,steps)
    endTime = time.time()

    print("{:n}, \t{:.6f}, \t{:.6f}, \t{:.6f}".format(
        num, loadTime-startTime, endTime-loadTime, endTime-startTime))


print("num, \tload time, \trun time, \ttotal time\n")
for t in tests:
    timeit(*t)

