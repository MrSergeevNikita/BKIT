import time
import contextlib
class cm_timer_1:

    def __enter__(self):
        self.s_time = time.time()

    def __exit__(self, ex1, ex2, ex3):
        print(time.time() - self.s_time)

@contextlib.contextmanager
def cm_timer_2():
    s_time = time.time()
    yield
    print(time.time() - s_time)