import re
f_name=input("Enter the First name --> ")
pattern=r"^[a-z][a-zA-z]{2,}$"
if re.match(pattern,f_name):
    print("Its a Valid Name")
else:
    print("Its a In-valid Name")