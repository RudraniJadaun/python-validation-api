# email=input("enter the email: ")
def check_email(email):
    x=0
    y=0
    if(len(email)>=0):
        if email[-3]=="." or email[-4]==".":
            if email[0].isalpha():
               for x in email:
                    if email.isspace():
                        x=1
                        print("by x")
                    if x=="_" or x=="*":
                        y=1
                        print("by y")
                    if x==1 or y==1:
                        print("a syntax error")
                    else:
                        if not email.isdigit():
                            pass
                        else:
                            print("there should we a combination of number and characters")
            else:
                print("the first letter should be a alphabet")
        else:
            print("the extension error")    
    else:
        print("the length issue!")       

# check_email(email)