import random 

print ("starting password generator....")

characters="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_len= int(input("enter the password length: "))

password=[];

for i in range (password_len):
    password.append(random.choice(characters))

password=''.join(password)
print("Your new password is: "+password)