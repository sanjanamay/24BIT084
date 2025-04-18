def fun():
    print("fun():")

def disp():
    print("disp():")

def msg():
    print("msg():")

functions = [fun, disp, msg]

for func in functions:
    func()
