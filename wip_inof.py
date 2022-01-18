from ast import Continue
from asyncore import write
import requests
import json
import time

while(True):
    ip_address = input("Enter the Ip adress:- ")
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print("note:- add '.txt' in the end")
    output_txt = input("Enter the output file name:-")
    txt = open(output_txt, "w+")
    txt.write(str(result))
    print("Type yes to start again type no to close")
    clappli = input("You want to use more?:- ")

    if "yes" in clappli:
        print("Starting again in 3 sec...")
        time.sleep(3)
        Continue
    elif "no" in clappli:
        print("Bye Bye hope see you again")
        break
    elif "Yes" in clappli:
        print("Starting again in 3 sec...")
        time.sleep(3)
        Continue
    elif "No" in clappli:
        print("Bye Bye hope see you again :)")
        break
    else:
        print("Choose a valid option!")
        put = input("you want to exit?:- ")
    if "yes" in put:
        print("Bye Hope see you again")
        break
    else:
        Continue