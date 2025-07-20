x = "stupid"
y = "frustated"
def func():
    y = "fine" #local variable y
    global x #global variable x
    x = "Awesome"
# before calling funtions 
print("someone is " + y)
print("someone is " + x)
func()
print("I'm " + x)
print("I'm " + y)