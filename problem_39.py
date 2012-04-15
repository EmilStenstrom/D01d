import threading

# Implementation of SafeFile
class SafeFile:
    lock = threading.Lock()

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        SafeFile.lock.acquire()
        return open(self.filename, self.mode)

    def __exit__(self, ty, val, tb):
        SafeFile.lock.release()
        return False

# How to use SafeFile
class MyThread(threading.Thread):
    def run(self):
        with SafeFile("counter.txt", "r+") as f:
            cnt = int(f.read().strip())
            print "Read count %s from file" % cnt
            f.seek(0)
            f.write(str(cnt + 1))
            print "Wrote count %s to file" % str(cnt + 1)

for x in xrange(5):
    MyThread().start()
