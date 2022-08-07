from threading import Thread
from time import sleep

mat=[[1,2,3],[4,5,6],[7,8,9]]

def mat_threaded_function(mat):
    rng1=int(input("Enter the range "))
    rng2=int(input("Enter the range "))
    for i in range(3):
        for j in range(3):
            if(rng2>int(mat[i][j])>rng1):
                print(mat[i][j])
        sleep(1)

if __name__ == "__main__":
    thread = Thread(target = mat_threaded_function, args = (mat, ))
    thread.start()
    thread.join()