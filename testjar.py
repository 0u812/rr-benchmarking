import time 
import psutil

# poll cpu every 0.25 seconds
pollTime=0.25

def getJarnacProcess():
    procs = psutil.get_process_list()
    for p in procs:
        try:
            if p.name().find('Jarnac') >= 0:
                return p
        except psutil.AccessDenied:
            pass
    raise Exception("Jarnac does not appear to be running")


def timeJarnac():
    j = getJarnacProcess()
    start = time.time()
    end = 0

    while True:
        time.sleep(pollTime)
        if j.cpu_percent() < 0.25:
            end = time.time()

            # make sure its done
            time.sleep(2)
            
            if j.cpu_percent() < 0.25:
                break

    

    return end-start

