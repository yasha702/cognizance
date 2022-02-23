#Question-4
#Check if the the number is palindrome
a=int(input("Enter any number:"))
temp=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(temp==rev):
    print("The given number is a palindrome!")
else:
    print("The given number isn't a palindrome!")