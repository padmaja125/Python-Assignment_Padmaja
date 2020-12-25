# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.
x = int(input("Enter the number : "))
if x != 0 :
    if x % 3 == 0 and x % 5 == 0:
        print ("Consultadd - Python Training")
    elif x % 3 == 0:
        print ("Consultadd")
    else :
        print("Python Training")
else:
    print ("enter the proper number")

# Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average

select = int(input("Enter the number from (1-5): "))
if select <=5 and select >= 0:
    if select == 1:
        print("Addition")
        x = int(input(" Enter the 1st value : "))
        y = int(input("Enter the 2nd value : "))
        z = x + y
        if z > 0 :
            print(x, "+", y ,"gives", z)
        else :
            print("Negative")
        
    elif select == 2:
        print("Subtraction")
        x = int(input(" Enter the 1st value : "))
        y = int(input("Enter the 2nd value : "))
        z = x - y
        if z > 0:
            print(x, "-", y ,"gives", z)
        else :
            print("Negative")
    elif select == 3:
        print("Division")
        x = int(input(" Enter the 1st value : "))
        y = int(input("Enter the 2nd value : "))
        z = x / y
        if z > 0:
            print(x, "/", y ,"gives", z)
        else :
            print("Negative")    
    elif select == 4:
        print("Multiplication")
        x = int(input(" Enter the 1st value  : "))
        y = int(input("Enter the 2nd value : "))
        z = x * y
        if z > 0:
            print(x, "*", y ,"gives", z)
        else :
            print("Negative")
    else :
        print("Average")
        x = int(input(" Enter the 1st value  : "))
        y = int(input("Enter the 2nd value : "))
        z = (x + y)/ 2
        if z > 0:
            print(x, y ,"makes a average of ", z)
        else :
            print("Negative")
else:
    print("you entered wrong option")
    
# Write a program in Python to implement the given flowchart
a, b, c = 10, 20, 30
avg = (a + b + c) / 3
if avg > a and avg > b and avg > c :
    print(avg, "is greater than a =", a, ", b = ", b, ' and c = ', c)
elif avg > a and avg > b :
    print(avg, "is greater than a = ", a, ' and b = ', b)
elif avg > a and avg > c :
    print(avg, 'is greater than a = ', a, ' and c = ', c)
elif avg > b and avg > c :
    print (avg, " is greater than b =", b, ' and c = ', c)
elif avg > a :
    print (avg, " is greater than a =", a)
elif avg > b :
    print(avg, "is greater than b = ", b)
else :
    print (avg, " is greater than c = ", c)

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

print ("You entered the loop")
x = 1
while x > 1 :
    x = int (input("Enter the number : "))
    if x > 0:
        print (" Good going")
        continue 
    else :
        print ("It's over")
        break
