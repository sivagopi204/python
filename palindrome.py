#Write a program that declares an integer and initializes it to a four digit number. The program prints true if it is a palindrome; otherwise it prints false.
#A palindrome is a number which when read in the reverse direction is the same as the original number. For example, 1771 is a palindrome. 
#sample output:
#    The number is 1771. Palindrome test: true.

num1 = input("Enter a four digit number:")
num2 = num1[::-1]
num1 = int(num1)
num2 = int (num2)

if num1 == num2:
    print ("The number %s is Palindrome" %num1)
else:
    print ("The number %s is not a palindrome" %num1)

