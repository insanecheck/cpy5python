#calc cylinder volume
g = input("Enter unit of measurement (cm/km/m) : ")
print ()
a = input("Enter height of cylinder: ")
height = float(a)
print ()
b = input("Enter radius of cylinder: ")
radius = float(b)
print ()
import math
c = "{0:<.3f}".format(float( math.pi * radius * radius * height))
print("The volume is: " + str(c) + " " + str(g) + chr(0x00B3))
print ()
print ("\u00A9"+"NeoWeiLu")

