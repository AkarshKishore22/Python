val = int(input("Enter the value "))


def square(num):
    return num * num


quad = lambda n: square(square(n))

print(quad(val))