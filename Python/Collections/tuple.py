tp = ('a','b','c')
# tp.append('d')  # This will raise an AttributeError since tuples are immutable

y = list(tp)
print(tp)
print(y)
y.append('d') 
print(y)
tp = tuple(y)
print(tp)


x = ("hello",1,2.3,)#dont forget the comma at the end of the tuple
tp += x  # Concatenating tuples
print(tp)



# what is we need to tremove something from the tuple?
# Tuples are immutable, so we cannot remove elements directly.
# However, we can convert it to a list, remove the element, and convert it back
print(tp)
y = list(tp)
y.remove(2.3)
print(y)
print(tp)
tp = tuple(y)
print(tp)