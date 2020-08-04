import threading

NUM = 0
local = threading.local()
INIT_N = 3


def run(n):
    global NUM
    NUM = NUM + n + 1
    NUM = NUM - n


def run_thread_loc(n):
    local.x = local.x + n + 1
    local.x = local.x - n


def run_loc(x, n):
    x = x + n + 1
    x = x - n


def func(n):
    local.x = 2 + n
    for i in range(100000):
        run(n)
        run_thread_loc(n)
        run_loc(INIT_N, n)
    print('%s-value: %d' % (threading.current_thread().name, local.x))


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(6,))
    t2 = threading.Thread(target=func, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('NUM = ', NUM)
    print('INIT_N = ', INIT_N)
