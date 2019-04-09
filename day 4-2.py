lower = 0
upper = 10000
a=[]
b= []
for num in range(lower,upper + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           if num<1000:
               a.append(num)
           else:
                b.append(num)
                print(num)
               
print("The prime numbers between 0 to 1000 are", a)
print("The prime numbers between 1000 to 10000 are", b)
