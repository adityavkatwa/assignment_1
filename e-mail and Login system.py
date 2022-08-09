import re
pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email_id = ''
def Register():
    emailSet = 0
    pwSet = 0
    while(emailSet == 0):
        email_id = input("Enter your email ID to register: ")
        if re.search(pattern, email_id):
            print("accepted")
            emailSet = 1
        else:
            print(f"{email_id} is Invalid.")
    print("email set")

    while(pwSet==0):
        Password = input("Enter the password to registor: ")
        if ((len(Password)<=5) or (len(Password)>16)):
            print("Password should contain more than 5 characters and should not contain more than 16 characters ")
            pwSet = 0
            break
        if not re.search('[A-Z]', Password):
            print("Password should contain minimum one uppercase letter")
            break
        if not re.search('[a-z]', Password):
            print("Password should contain minimum one lowercase letter")
            break
        if not re.search('[0-9]', Password):
            print("Password should contain minimum one digit")
            break
        if not re.search('[!@#%&*_+=$]', Password):
            print("Password should contain minimum one special character !@#%&*_+=$ ")
            break
        else:
            print("accepted")
            pwSet = "1"

    if pwSet=="1":
        db1 = open("database.txt", "a")
        db1.write(f"\n{email_id} , {Password}")
        db1.close()
        print("Registered")
        pass

def Login():
    success = False
    email_id = input("Enter your email ID to login: ").strip()
    Password = input("Enter the password to login: ").strip()

    db = open("database.txt", "r")
    for i in db:
        a = ''
        b = ''
        try:
            a, b = i.split(" , ")
            b = b.strip()
        except:
            pass

        if(len(a)>5 and len(b)>5):
            if(a == email_id and b == Password):
                success = True
                break
    db.close()

    if(success):
        print("Login Sucessful")
        z = 0
        while(z==0):
            xz = input("wanna logout? y/n:")
            if(xz in ["y","Y","Yes","yes","s","S"]):
                print("----------------------------------------------")
                print("logout success")
                print("----------------------------------------------")
                z = 1
            else:
                print("retry")

    else:
        print("Login error\n")
        reset_pwd = input("wanna retrieve your password y/n:")
        if(reset_pwd == "y"):
            forgot_password()
        print("-----------------------------------------------")

    Home()

def forgot_password():

    email1 = input("Enter your e-mail id to get the password:").strip()
    if(len(email1)>5):
        with open("database.txt","r") as users:

            for user in users:
                try:
                    a1, b1 = user.split(" , ")
                    a1 = a1.strip()
                    b1 = b1.strip()
                except:
                    continue
                if(email1 == a1):
                    print(f"Your password is for {email1} is {b1}\n--------------------------------------------------------")
    else:
        print("user not found")


def Home():
    option = input("Register\nLogin\nLogout\nEnter one:")
    if(option == "Register"):
        Register()
    elif(option == "Logout"):
        quit()
    else:
        Login()

Home()








