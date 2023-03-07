#This prgram is to check your passowrd is it is more than 8 characters
username = input("Enter your name")
password = input("Enter your password")
hiddenPassword =  '*' * len(password)
numberOfCharacter = len(password)
while len(password) < 8:
    print("Your password must be more than 8 characters")
    password = input("Enter your password")
    numberOfCharacter = len(password)


print(f"Hello {username} your password is{hiddenPassword} ")
revealPassword = input("Do you want to see your password (enter y/n)?")
if revealPassword == 'y':
    print(f'Your password is {password}')