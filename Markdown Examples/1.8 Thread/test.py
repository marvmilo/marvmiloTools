import time
import marvmiloTools as mmt

def function(string):
    while True:
        print(string)
        time.sleep(1)

thread_id = mmt.thread(function, "hello world")
print(mmt.threads[thread_id].is_alive())

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    for id in mmt.threads:
        mmt.threads[id].stop()