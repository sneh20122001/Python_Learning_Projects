import re 

email_condition = r"^[a-zA-Z][\w._]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

email = input("Enter Your Email: ")

if re.match(email_condition, email):
    print("Valid Email ID")
else:
    print("Wrong Email ID")