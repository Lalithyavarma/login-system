
def Registration():
    db = open("database.txt",'r')
    d =[]
    f =[]
    for i in db:
        q , w = i.split(",")
        d.append(q)
        f.append(w)
    data = dict(zip(d, f ))

    def pswrd():
        a, b, c, u= 0, 0, 0, 0
        Password = input("create your password: ")
        Confirmpassword = input("confirm your password: ")
        if Password != Confirmpassword:
            print("password donot match,restart")
            pswrd()
        else:
            if (len(Password) >= 5) and (len(Password) <= 13):
                for i in Password:
                    if i.isalpha():
                        if i.isupper():
                            a=1
                    elif i.isalpha():
                        if i.islower():
                            b=1
                    elif i.isdigit():
                        if i.isdigit():
                            c=1


                    elif i in ('[@_!$%^&*()<>?/\|}{~:]#'):
                        u = 1

                if not a==1 ^ b==1 ^ c==1 ^ u==1:
                    print("password should contain one capital,small,digit ,one special character")
                    pswrd()


                else:
                    db = open("database.txt", "a")
                    db.write(Username + "," + Password + "\n")
                    print("registration success!")
            else:
                print("password length should be more than 5 and less than 13 digits")
                pswrd()

    k, j, l = 0, 0, 0

    Username = input("create a username: ")
    if Username not in d:
        if len(Username) >= 6:
            if Username[0].isalpha():
                if ("@" in Username) and (Username.count("@") == 1):
                    if (Username[-4] == ".") ^ (Username[-3] == "."):
                        if "@." not in Username:
                            for i in Username:
                                if i.isspace():
                                    k = 1
                                elif i.isalpha():
                                    if i.isupper():
                                        j = 1

                                elif i.isdigit():
                                    continue
                                elif i == "_" or i == "." or i == "@":
                                    continue
                                else:
                                    l = 1
                            if k == 1 or j == 1 or l == 1:
                                print("username should not have capital letters, space,any special characters")
                                Registration()
                            else:
                                pswrd()

                        else:
                            print("@ and . should not be side by side, restart")
                            Registration()
                    else:
                        print("wrong username,(ex:xyz@gmail.com),restart")
                        Registration()
                else:
                    print("enter correct username,should have one @, restart")
                    Registration()
            else:
                print("username should start with alphabet,restart")
                Registration()

        else:
            print("wrong username,(ex:xyz@gmail.com),restart")
            Registration()

    else:
        print("username already exists, restart")
        Registration()



def login():
    db = open("database.txt", 'r')
    def passwrd():
        a, b, c = 0, 0, 0
        Password = input("create your password: ")
        Confirmpassword = input("confirm your password: ")
        if Password != Confirmpassword:
            print("password donot match,restart")
            passwrd()
        else:
            if (len(Password) >= 5) and (len(Password) <= 13):
                for i in Password:
                    if i.isalpha():
                        if i.isupper():
                            a = 1
                    elif i.isalpha():
                        if i.islower():
                            b = 1
                    elif i.isdigit():
                        c = 1
                if a == 1 or b == 1 or c == 1:
                    db = open("database.txt", "a")
                    data[Username]= Password
                    db.write(Username + "," + Password + "\n")

                else:
                    print("password should have a capital, small , digit and one special character")
                    passwrd()
            else:
                print("password length should be more than 5 and less than 13 digits")
                passwrd()

    d = []
    f = []
    for i in db:
         q, w = i.split(",")
         d.append(q)
         f.append(w)
    data = dict(zip(d, f))
    def forgotpassword(option=None):
        def createnewpassword():
            Username = input("please enter username:")
            if Username in d:
                Password = input("please enter your new password:")
                passwrd()

            else:
                print("username does not exist,register")
                Registration()
        def retrievepassword():
            Username = input("please enterusername:")
            if Username in d:
                Password = data[Username]
                print("here is you password:",Password)
            else:
                print("username does not exist,register")
                Registration()

        option = input("createnewpassword | retrievepassword:")
        if option == "createnewpassword":
            createnewpassword()
        elif option == "retrievepassword":
            retrievepassword()
        else:
            print("choose a option")
            forgotpassword()

    Username = input("enter username: ")
    Password = input("enter password: ")
    if not len(Username or Password)<1:
        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("login success")
                        print("hi,", Username)
                    else:
                        print("password incorrect")
                        forgotpassword()

                except:
                    print("incorrect username or password")
                    forgotpassword()
            else:
                print("username doest not exist,register")
                Registration()
        except:
            print("login error")
            forgotpassword()




def home(option=None):
    option = input("login| Registration:")
    if option == "login":
        login()
    elif option == "Registration":
        Registration()
    else:
        print("please enter a option")
        home()


home()









