#Write a program that declares and initializes a character variable.
#It prints true if the character corresponds to a digit i.e. one of 0, 1, 2, ..., 9; otherwise it prints false.
#Extend the program to check if it is an alphabet (i.e. one of a, b, ..., z or A, B, ..., Z) or a digit. Such characters are called alphanumerics.

ch = "1"
ch1=ch.isdigit()
ch2 = ch.isalpha()
if ch1 == True:
    print ("%s is a digit ?:" %ch, ch1)
if ch2 == True:
    print ("%s is a alphabet ?:" %ch, ch2)
