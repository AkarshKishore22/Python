def printInitials(name):
    if(len(name) == 0):
        return
    print(name[0].upper()),
    for i in range(1, len(name) - 1):
        if (name[i] == ' '):
            print (name[i + 1].upper()),
 
def main():
    name = input("Enter Your Name")
    printInitials(name)
 
if __name__=="main_":
            main()