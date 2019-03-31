#Write a program that declares a double number and initializes it to a positive real number.
#The program prints the integer part, fractional part, and the nearest integer of this number.
#Assume that the nearest integer of X.5 is X+1 where X is a non-negative integer. For example,
#if the number is 4.678 the program should produce the following output.
#    	The integer part of 4.678 is 4.
#	The fractional part of 4.678 is 0.678.
#	The nearest integer to 4.678 is 5.
#Note that the second line may not come out exactly as 0.678

double = 12.0891
print("The Integer part of %s is %s" %(double,int(double)))
print("The fractional part of %s is %s"%(double, double-int(double)))
print("The nearest integer to %s is %s"%(double,round(double)))
