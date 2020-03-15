#Ray Peters

n= int(input("Enter integer: "))
m= int(input("Enter another Interger: "))


def multiple_(n,m):

    if n % m == 0:
        return True
    else:
        return False
    

         
print(multiple_(n,m))