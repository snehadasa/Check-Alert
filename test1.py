#!/usr/bin/python3
from sys import argv
import requests
import json
import getpass
from apscheduler.schedulers.blocking import BlockingScheduler


id = 0


def get_user_info():
    key = input('\nVisit: https://intranet.hbtn.io/dashboards/my_tools\nand enter your API Key from the bottom of the page: \n')
    print()
    user_id = input('Enter your Holberton ID: \n')
    print()
    # psw = input("Enter your Holberton password. (We do not store it)\n")
    psw = getpass.getpass(prompt='Enter your Holberton password.' + '(We do not store it)\n')
    print()
    project = input("Which project? (id at the end of project's URL\n")
    print()
    slack_channel = input('Please visit https://checkalert.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks\n Select a channel and paste the link here: ')
    print()
    return key, user_id, psw, project, slack_channel
key, user_id, psw, project, slack_channel = get_user_info()
email = user_id + '@holbertonschool.com'
user_data = {'api_key': key, 'email': email, 'password': psw, 'scope': "checker"}
url = 'https://intranet.hbtn.io/users/auth_token.json'
auth = requests.post(url=url, data=user_data)
print(auth.json())
print()
token = auth.json().get('auth_token')
url_p = 'https://intranet.hbtn.io/projects/' + project + '.json?auth_token=' + token
pj = requests.get(url=url_p)
print('requesting project info')
i = 0
flag = 0
while (i < len(pj.json().get('tasks'))):
    print('checking if checker will be available')
    if pj.json().get('tasks')[i].get('checker_available') is True:
            flag = 1
            task_id = pj.json().get('tasks')[i].get('id')
            break
            print('saving task number {}'.format(task_id))
    i += 1
if flag == 0:
    print("No checker for project")
    exit()

def timed_job():
    url_request = 'https://intranet.hbtn.io/tasks/' + str(task_id) + '/start_correction' + '.json?auth_token=' + str(token)
    print(url_request)
    request_dict = requests.post(url=url_request).json()
    request_id = request_dict.get('id')
    if request_id != 0:
        checkers = "Checker is out"
        payload = {"text": checkers}
        requests.post(slack_channel, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        exit()
    else:
        checkers = "Checkers for " + pj.json().get('name') + " is not available"
        payload = {"text": checkers}
        requests.post(slack_channel, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        from time import sleep
        sleep(10)

        # sched.configure(options_from_ini_file)
  
while (1):
  timed_job()
  print('The checker is out and a message has been sent to slack.')
exit()
