user_password='Irum1983'
attempts=0
password= input('Please enter your password: ')
while password != user_password:
    if attempts < 2:
        print("Incorrect password, try again")
        password= input('Please Enter again')
        attempts+=1
    else:
        print("Your account is blocked")
        break
else:
    print('Welcome')