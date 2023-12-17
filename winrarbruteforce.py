import rarfile
import os


file_path = input("Enter the path to your WinRAR file: ")
password_list_path = input("Enter the path to your password list file: ")

with open(password_list_path, 'r') as file:
    password_list = [line.strip() for line in file]

output_directory = os.path.dirname(file_path)

correct_password = None

for password in password_list:
    try:
        with rarfile.RarFile(file_path, 'r') as rf:
            rf.setpassword(password.encode('utf-8'))
            rf.testrar()
        print(f"Password found: {password}")
        correct_password = password
        break
    except rarfile.RarWrongPassword:
        print(f"Wrong password: {password}")
    except rarfile.RarCannotExec:
        print(f"This one is the key: {password}")
        break




