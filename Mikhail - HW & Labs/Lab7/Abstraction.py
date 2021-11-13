from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
        print('Passed value: ', x)

    @abstractmethod
    def task(self):
        print('We are inside Absclass task')

class test_class(Absclass):
    def task(self):
        print('We are inside test_class task')

class example_class(Absclass):
    def task(self):
        print('We are inside example_class task')

test_obj = test_class()
test_obj.task()
test_obj.print(100)

example_obj = example_class()
example_obj.task()
example_obj.print(200)

print('test_obj is instance of Absclass? ', isinstance(test_obj, Absclass))
print('example_obj is instance of Absclass? ', isinstance(example_obj, Absclass))