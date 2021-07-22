

import requests
import os


def processdata(time):
    commd = 'sudo date -s "'+time+"\""
    print(commd)
    tmp = os.popen(commd).readlines()
    print(tmp)
    commd2 = 'sudo hwclock --systohc'
    tmp = os.popen(commd2).readlines()
    print(tmp)

def getmydata():

    try:
        url = 'http://192.168.199.188:9880/heath-indicator/time-sync'


        try:
            resp = requests.get(url)
        except Exception as e:
            print(e)

        if (resp.status_code == 200):
            print('\033[1;36m get success!! \033[0m')
            mydata = resp.json()
            time = mydata['msg']
            processdata(time)
        if (resp.status_code != 200):
            # upload failed ,save data to csv
            print('\033[1;35m get failed ,save to csv \033[0m')
        json = resp.json()
        print(json)
    except BaseException as e:
        print(e)


getmydata()


