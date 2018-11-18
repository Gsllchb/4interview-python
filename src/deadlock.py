import threading
import time


def main():
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    t1 = threading.Thread(target=foo, args=(lock1, lock2))
    t2 = threading.Thread(target=foo, args=(lock2, lock1))
    t1.start()
    t2.start()


def foo(lock1, lock2):
    lock1.acquire()
    time.sleep(1)
    lock2.acquire()
    lock2.release()
    lock1.release()


if __name__ == '__main__':
    main()
