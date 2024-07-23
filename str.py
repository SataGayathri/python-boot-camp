#strings
#is alpha
#is digit
#is upper
#is lower
#lower case
#upper case
#title case
#swap case""""""

str="gayathri"
str2="      gunnu"
str4="12345"
a=str.isupper()
b=str.islower()
c=str.isalpha()
d=str4.isdigit()
e=str.lower()
f=str.upper()
g=str.title()
h=str.swapcase()


print("isupper is",a)
print("islower is",b)
print("isalpha is",c)
print("isdigit is",d)
print("upper is",e)
print("lower is",f)
print("title is",g)
print("swapcase is",h)
print(str.replace('a','z'))
print(str.split('a'))
print(str2.strip())
print(str2.rstrip())
print(str2.lstrip())
print(str4.isnumeric())
print(str.isalnum())



