import re

pattern=r"^[A-Z][a-zA-z]{2,}$"
emailpattern=r"^[\w_.]@[a-zA-z].[a-z]{3}.[a-z]{2}$"

class Invalid(Exception):
    pass

def first_name(f_name,l_name):
    if not (re.match(pattern,f_name) and re.match(pattern,l_name)):
        raise Invalid ("Firstname and Lastname should start with cap and should be more than 3 letters")
    return f"{f_name} {l_name} is a valid Name"
def email(email):
    if not (re.findall(pattern,email)):
        raise Invalid ("Email should be in this format E.g. abc.xyz@bl.com")
    return f"{email} is a valid Name"

try:
    x=input("Enter the First name --> ")
    y=input("Enter the Last name --> ")
    z=input("Enter the Email--> ")
    print(first_name(x,y))
    print(email(z))
except Invalid as e:
    print(e)