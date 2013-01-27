#Prompt Question
k = input("Enter Number:")

#Calculation
a = int(k)
b = a % 10
c = (( a % 100 ) - b) // 10
d = ( a - ( a % 100 )) // 100
e = b + c + d
print ()

#Answer
print("The Answer Is:"+str(e))
print()

#Acknowledgement(s)
print((u"\u00A9")+"Neo Wei Lu 2013")

