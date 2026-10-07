class Chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""Welcome to Chatbook! How would you like to proceed? 
        1.press 1 to login
        2.press 2 to signup 
        3.press 3 to write a post
        4.press 4 to message a friend
        5.press any other key to exit""")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_posts()
        elif user_input=="4":
            self.send_message()
        else:
            exit()
    def signup(self):
        email=input("Enter your email: ")
        pwd=input("Enter your password: ")
        self.username=email
        self.password=pwd
        print('signup successful  ')
        print('\n')
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print('please signup frist 1 is the main menu')
        else:
            uname=input('Enter your email/username: ')
            pwd=input('Enter your password:')
            if uname==self.username and pwd==self.password:
                print('login successful')
                self.loggedin=True
            else:
                print('invalid credentials')
        print('\n')
        self.menu()
    def my_posts(self):
        if self.loggedin==True:
            txt=input('Enter your post : ')
            print(f'my post is {txt}')
        else:
            print('please login first to post something')
        print('\n')
        self.menu()
    def send_message(self):
        if self.loggedin==True:
            msg=input('enter your message: ')
            friend=input('enter your friend name')
            print(f'message sent to {friend} is msg {msg}')
        else:
            print('please login first to send a message')
        print('\n')
        self.menu()

#user1=Chatbook()

