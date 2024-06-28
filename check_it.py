from email_validation import check_email

class varify():
    def __init__(self,email):
        self.email=email
    
    def check(self):
        check_email(self.email)

collection=varify(input("enter the email: "))
collection.check()

# def verify(email):
#     check_email(email)
#     print("register")

# verify(input("enter the email: "))