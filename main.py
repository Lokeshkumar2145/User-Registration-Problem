import re
f_name=input("Enter the First name --> ")
l_name=input("Enter the Last name --> ")
pattern=r"^[A-Z][a-zA-z]{2,}$"
if re.match(pattern,f_name) and re.match(pattern,f_name):
    print("Its a Valid Name")
else:
    print("Its a In-valid Name")


