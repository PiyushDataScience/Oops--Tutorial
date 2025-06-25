class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook!
                           1.Press 1 to signup
                           2.Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to msg a friend
                           5. Press E to exist
                           """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your Email Here -->")
        password = input("Setup your Password -->")
        self.username = email
        self.password = password
        print("Succesfully signed up \n")
        print(self.menu())

    def signin(self):
        if self.username == "" and self.password == "":
            print("Pls signup first by pressing 1 in main menu")
        else:
            username = input("enter your email/username here -->")
            password = input("enter your password here -->")

            if self.username == username and self.password == password:
                print("You have successfully signed in")
                self.loggedin = True
            else:
                print("Pls input correct crendential")
        print("\n")
        print(self.menu())

    def my_post(self):
        if self.loggedin == True:
            txt = input("Whats in your mind :) -->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign in first to post something")

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your msg -->")
            print(f"Your {txt} have been send to your frnd")
