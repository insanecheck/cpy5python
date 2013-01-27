#prompt original unit
print("~Celsius, Kelvin or Fahrenheit~")

a = input("Original unit: ")
c = input("value: ")
d = float(c)
print()
#convert
if a == "celsius":
    g = "°F"
    k = "K"
if a == "fahrenheit":
    g = "°C"
    k = "K"
if a == "kelvin":
    g = "°C"
    k = "°F"
#what if...
    
if a == "celsius":
    e = "{0:<.1f}".format(float(d * 9 / 5 + 32))
    h = "{0:<.1f}".format(float(d + 273))
elif a == "fahrenheit":
    e = "{0:<.1f}".format(float((d - 32) / 9 * 5))
    h = "{0:<.1f}".format(float((d - 32) / 9 * 5 + 273))
elif a == "kelvin":
    e = "{0:<.1f}".format(float(d - 273))
    h = "{0:<.1f}".format(float(((d - 273) * 9 / 5) + 32 ))
#Answer
    
print("Your answer is: " + str(e) + str(g) + " or " + str(h) + str(k))
print ()

#Acknowledgements
print((u"\u00A9")+"Neo Wei Lu 2013")


