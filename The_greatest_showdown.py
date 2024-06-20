#Task 1: Identify the Greatest
#Write a Python program that prompts the user to enter three numbers. 
#The program should then identify and print out the largest number among the three.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
Largest_num = max(number1, number2, number3)
print("The Largest number is " +  str(Largest_num))



#Task 2: Identify the Smallest
#Extend your program from Task 1 to also determine the smallest 
#number among the three and print it out.

Smallest_num = min(number1, number2, number3)
print("The Smallest number is " +  str(Smallest_num))

#Task 3: Equality Check
#Enhance your program to handle cases where two or all of the numbers are equal. 
#The program should display appropriate messages like "Two numbers are equal 
#and the largest" or "All numbers are equal".

if number1 == number2:
    print("There are two numbers equal to each other and they are " + str(number1))
elif number2 == number3:
    print("There are two numbers equal to each other and they are " + str(number2))
elif number1 == number3:
    print("There are two numbers equal to each other and they are " + str(number1))
else: 
    print("No numbers are equal to each other")


#Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that
#"The smallest number is 3. The largest number is 4. There are two numbers equal
#to each other." Printing out which numbers are equal would be a great added bonus.
