def add(x,y):
    return x + y

def  sub(x,y):
    return x - y 


total = add(10,20)
print(total)

f = add  #add 함수에 대한 참조.
total = f(20,30)
print(total)

def test(f):   # f=add
    return f(30,40) #함수를 호출하겠다.

test(add)

