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
  psw = getpass.getpass(prompt='Enter your Holberton password.' +
                                  '(We do not store it)\n')
  print()
  project = input("Which project? (id at the end of project's URL\n")
  print()
  return key, user_id, psw, project
key, user_id, psw, project = get_user_info()
email = user_id + '@holbertonschool.com'
user_data = {'api_key':key, 'email': email, 'password': psw, "scope": "checker"}
url = 'https://intranet.hbtn.io/users/auth_token.json'
auth = requests.post(url=url, data=user_data)
print(auth.json())
print()
token = auth.json().get('auth_token')

sched = BlockingScheduler()
@sched.scheduled_job('interval', seconds=10)
def timed_job():
  url_p = 'https://intranet.hbtn.io/projects/' + project  + '.json?auth_token=' + token
  pj = requests.get(url=url_p)

  i = 0
  while (i < len(pj.json().get('tasks'))):
    if pj.json().get('tasks')[i].get('checker_available') is True:
      checkers = "Checkers is out"
      payload={"text": checkers}
      requests.post('https://hooks.slack.com/services/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', data=json.dumps(payload), headers={'Content\
-Type': 'application/json'} )
      exit()
    i += 1
  checkers = "Only manual for " + pj.json().get('name')
  payload={"text": checkers}
  requests.post('https://hooks.slack.com/services/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', data=json.dumps(payload), headers={'Content-Type': 'application/json'} )

# sched.configure(options_from_ini_file)
sched.start()
