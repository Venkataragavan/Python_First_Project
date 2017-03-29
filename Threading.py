import threading

class MyThread(threading.Thread):
    def run(self):
        for _ in range(5):
            print('Thread name : '+threading.currentThread().getName())

Thread1= MyThread(name='This is thread1!')
Thread2 = MyThread(name='This is thread2!')
Thread2.start()
Thread1.start()

