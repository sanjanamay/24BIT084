def fun():
    print("This is the fun function.")

def disp():
    print("This is the disp function.")

def msg():
    print("This is the msg function.")
function_list = [fun, disp, msg]
for function in function_list:
    function()
