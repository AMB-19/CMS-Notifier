import os
LoginID, Password = '', ''
if not os.path.exists("Qalam/login.txt"):
    LoginID = input('Enter CMS Login ID: ')
    Password = input('Enter Password: ')
    with open("Qalam/login.txt", 'w') as f:
        f.write(LoginID+'\n')
        f.write(Password+'\n')
else:
    with open("Qalam/login.txt", 'r') as f:
        LoginID = f.readline()
        Password = f.readline()
