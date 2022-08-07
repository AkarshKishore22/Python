from threading import Thread
from time import sleep

def O_threaded_fun(arg,arg2):
    for i in range(arg,arg2):
        if i%2!=0:
            print("T1-",i)

def P_threaded_fun(arg,arg2):
    for i in range(arg,arg2):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                print("T2-",i)

def A_threaded_fun(arg,arg2):
    for num in range(arg,arg2):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print("T3-",num)

sleep(1)
if __name__ == "__main__":
    thread = Thread(target = O_threaded_fun, args = (100,200 ))
    thread1 = Thread(target = P_threaded_fun, args = (200,300 ))
    thread2 = Thread(target = A_threaded_fun, args = (100,300 ))
    thread.start()
    thread.join()
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()