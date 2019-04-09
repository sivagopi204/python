#Write a function to print the binary representation of a given integer

#method by using inbuilt methods
a=int(input("please enter a number:"))
b=bin(a)
print (b)

#model 2 by using the recursive function
def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')

binary(a)
