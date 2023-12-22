number= int(input("enter a number"))
reverse=0
a=number
while(number > 0):
digit = number%10
reverse=reverse*10+digit
number = number//10
print("it is a palindrome number")
else:
print("not palindrome")


