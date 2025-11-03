email = input("Enter Your Email : ")
k, d, j = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in ["_", ".", "@"]:
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email ID - Due to space in email or Upper letter or other sign") 
                else:
                    print("Valid Email ID")
            else:
                print("Wrong Email ID - Due to not valid . char")
        else:
            print("Wrong Email ID - @ is not in email or more than 1")    
    else:
        print("Wrong Email ID - First letter is not valid")
else:
    print("Wrong Email ID - Due to len of Email")
