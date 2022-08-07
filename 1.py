from threading import Thread
from threading import Event

even_available = Event()
odd_available = Event()

def print_even():
    global limit
    global exit_prog
    global number

    while not exit_prog and number < limit:
        even_available.wait()
        print('T1', number)
        number = number + 1
        even_available.clear()
        odd_available.set()

def print_odd():
    global limit
    global exit_prog
    global number

    while not exit_prog and number < limit:
        odd_available.wait()
        print('T2', number)
        number = number + 1
        odd_available.clear()
        even_available.set()

if __name__ == "__main__":

    limit = 10
    exit_prog = False
    number = 0

    t1 = Thread(target=print_even)
    t2 = Thread(target=print_odd)

    even_available.set()

    t1.start()
    t2.start()

    t1.join()
    t2.join()