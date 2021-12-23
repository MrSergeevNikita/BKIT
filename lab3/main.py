import json
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

with open('data.txt', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(data):
    return sorted(list(Unique([key[value] for key in data
                                            for value in key if value.lower() == 'job-name'])))

@print_result
def f2(data):
    return list(filter(lambda profession: profession.lower().startswith('программист'), data))

@print_result
def f3(data):
    return list(map(lambda profession: profession + ' с опытом Python', data))

@print_result
def f4(data):
    return [profession + ', зарплата ' + str(salary)
    for profession, salary in zip(data, gen_random(len(data), 100000, 200000))]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

