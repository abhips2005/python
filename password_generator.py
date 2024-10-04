import string
import random

def password_generator(length,include_digits=True,include_spcl_char=True):
   letters= string.ascii_letters
   digits= string.digits if include_digits else ''
   spcl_chars= string.punctuation if include_spcl_char else ''

   all_chars= letters + digits + spcl_chars

   password=''.join(random.choice(all_chars) for _ in range(length))
   return password

pass_length=int(input("Enter the length of the password: "))
include_digits=input("Do you want to include digits im your password(y/n): ").lower()=='y'
include_spcl_char= input("Include special characters? (y/n): ").lower()=='y'

password= password_generator(pass_length,include_digits,include_spcl_char)
print("Generated password:", password)
