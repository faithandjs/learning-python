
import queue
import threading
import time

# ====================================================================================================
# CLASSES
# ====================================================================================================


class Person:
    amount = 0  # class variable

    def __init__(self, name, age, height=171):  # constructor
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self, ):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)


x = Person('Mike', 30)
print(x)

# ====================================================================================================
# INHERITANCE
# ====================================================================================================


class Worker(Person):

    def __init__(self, salary, name, age, height=171):
        super().__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        return super().__str__()+", Salary: {}".format(self.salary)

    def calc_yearly_salary(self):
        return self.salary * 12


worker1 = Worker(2000, "Moses", 43)


# ====================================================================================================
# OPERATOR OVERLOADING
# ====================================================================================================
# defining actions for the operators, __sub__ for subtract(-), __add__ for addition(+)


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __str__(self):
        return "x: {}, y:{}".format(self.x, self.y)


v1 = Vector(1, 3)
v2 = Vector(2, 4)
v3 = v1-v2
# print(v3)

# ====================================================================================================
# THREADING
# ====================================================================================================
# Helps us spead up our tasks with 'threads'


def func1():
    for x in range(10):
        print("One")


def func2():
    for x in range(10):
        print("two")


t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# run() doesnt run in parallel
# join() finishes the thread before proceeding with the code, like an await
# t1.join()

# print('otra hola')

# ====================================================================================================
# MULTI THREADING
# ====================================================================================================
# Locking - locks a global resource accessed by multiple threads

x = 8192
lock = threading.Lock()


def double():
    global x, lock  # global keyword lets you access and change a global variable
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x, 'Double')
        # sleep method tells the program to wait for x amount of secs, like an interval
        time.sleep(1)
    print("Reached the maximum")
    lock.release()


def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x, 'Half')
        time.sleep(1)
    lock.release()


# t1 = threading.Thread(target=half)
# t2 = threading.Thread(target=double)
# t1.start()
# t2.start()

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print("{} is trying to access!".format(thread_number))
    semaphore.acquire()
    print("{} was granted!".format(thread_number))
    time.sleep(10)
    print("{} is now releaseing!".format(thread_number))
    semaphore.release()


# for thread_number in range(1, 11):
#     # t = threading.Thread(target=access, args=(thread_number,))
#     # t.start()
#     time.sleep(1)

event = threading.Event()


def myFunc():
    print('waiting')
    event.wait()
    print('acting')


tt = threading.Thread(target=myFunc)
tt.start()

x = input('Do you want to trigger the event? \n(y/n)')
if x == 'y':
    event.set()
# else:

# ====================================================================================================
# DAEMON THREADS
# ====================================================================================================

path = "text.txt"
text = ""


def readFile():
    global path, text
    while True:
        with open("text.txt", 'r') as f:
            text = f.read()
        time.sleep(3)


def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


dt1 = threading.Thread(target=readFile, daemon=True)
dt2 = threading.Thread(target=printLoop)

dt1.start()
dt2.start()


# ====================================================================================================
# QUEUES
# ====================================================================================================

# queue handles an array or set of numbers and dishes the resources one at a time so there are no repititions or skipped numbers/resources

q = queue.Queue()
ql = queue.LifoQueue()
qp = queue.PriorityQueue()
numbers = [10, 20, 30, 40, 50, 60, 70]

for number in numbers:
    q.put(number)
    ql.put(number)

qp.put((20, 7))
qp.put((10, 17))
qp.put((200, 1))
qp.put((2, 'otra'))

print(qp.get())
print(qp.get())
print(qp.get())
# print(ql.get())
