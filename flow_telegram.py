#!/usr/bin/python3
import os
import time
import requests
import json

def get_msm_code():
    try:
        id = get_telephone_number()
        id[2]
        querystring = {"metod": "get_sms", "country": "ID", "service": "opt29", "id": id[2],
                       "apikey": "ZOpFYmG5MxgHop0p3S1ZiHaG8bMZQ0"}

        url = "http://smspva.com/priemnik.php"

        headers = {
            'User-Agent': "PostmanRuntime/7.18.0",
            'Accept': "/",
            'Cache-Control': "no-cache",
            'Postman-Token': "078f547e-ac35-4134-a504-1b2b6b277a45",
            'Host': "smspva.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
        }
        response = requests.request("GET", url, headers=headers, params=querystring, timeout=4)
        temp = json.loads(response.text)
        tempInfo = (temp['sms'])
        return tempInfo
    except Exception as e:
        print(e)

def get_telephone_number():
    try:
        querystring = {"metod": "get_number", "country": "ID", "service": "opt29",
                       "apikey": "ZOpFYmG5MxgHop0p3S1ZiHaG8bMZQ0"}

        url = "http://smspva.com/priemnik.php"

        headers = {
            'User-Agent': "PostmanRuntime/7.18.0",
            'Accept': "/",
            'Cache-Control': "no-cache",
            'Postman-Token': "110537a0-ae69-404d-ac73-e1be5c581e92",
            'Host': "smspva.com",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
        }
        response = requests.request("GET", url, headers=headers, params=querystring, timeout=4)
        temp = json.loads(response.text)
        tempInfo = (temp['CountryCode'], temp['number'], temp['id'])
        return tempInfo
    except Exception as e:
        print(e)


def log_flow_telegram():
    infonumber = get_telephone_number()
    infonumber[0]
    print(infonumber[0])
    infonumber[1]
    print(infonumber[1])
    count = 0

    path = "D://Program Files//Nox//bin"
    os.chdir(path)
    device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
    connect = os.popen("adb connect " + device).read()
    print(connect)
    os.system("adb shell monkey -p org.telegram.messenger -c android.intent.category.LAUNCHER 1")
    time.sleep(3)
    os.system("adb shell input tap 430 1400")
    time.sleep(1)
    os.system("adb shell input tap 440 360")
    time.sleep(1)
    while count < 11:
        os.system('adb shell input keyevent 67')
        count += 1
    time.sleep(1)
    os.system('adb shell input text "' + infonumber[0] + '' + infonumber[1] + '"')
    time.sleep(1)
    os.system("adb shell input tap 840 110")


log_flow_telegram()