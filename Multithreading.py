#calculate the sum of a range using two threads
import threading

class SampleThread(threading.Thread):
     def __init__(self, from_var, to_var):
         super(SampleThread, self).__init__()
         self.from_var = from_var
         self.to_var = to_var
         self.res = 0

     def run(self):
         for i in range(self.from_var, self.to_var):
             self.res += i

thread1 = SampleThread(0, 10000)
thread2 = SampleThread(10000, 50000)
thread1.start()
thread2.start()
# This waits until the thread has complete
thread1.join()
thread2.join()
# At this point, both threads have completed
result = thread1.res + thread2.res
print(result)