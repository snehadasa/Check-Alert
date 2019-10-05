#!/usr/bin/python3
'''Module for the amazing Check Alert'''
from sys import argv
import requests
import json
import getpass


write_file = __import__('write_file').write_file
read_file = __import__('read_file').read_file


def get_user_info():
    '''Gets HBTN API key, username, pw, slack channel from user input'''
    input_flag = 0
    try:
        api_file = read_file('APIkey')
        key = api_file
        print('\nUsing API key: ' + key)
    except:
        while (input_flag == 0):
            key = input(
                '\nVisit: https://intranet.hbtn.io/dashboards/my_tools\n' +
                'and enter your API Key from the bottom of the page: \n')
            if len(key) < 32:
                print('Error: Invalid API Key\n')
            else:
                input_flag = 1
        write_file("APIkey", key)

    print()
    input_flag = 0
    while (input_flag == 0):
        user_id = input('Enter your Holberton ID: \n')
        try:
            int(user_id)
            input_flag = 1
        except:
            print('Error: Invalid ID\n')

    print()
    psw = getpass.getpass(prompt='Enter your Holberton password.' +
                          ' (We do not store it)\n')

    input_flag = 0
    while (input_flag == 0):
        project = input("Which project? (id at the end of project's URL)\n")
        try:
            int(project)
            input_flag = 1
        except:
            print('Error: Invalid Project ID\n')
        if (len(project)) > 4:
            print('Error: Invalid Project ID\n')
            input_flag = 0
    print()

    try:
        slack_channel = read_file('slack_channel')
        print('Using slack channel: ' + slack_channel)
    except:
        slack_channel = input('Please visit ' +
                              'https://checkalert.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks\n' +
                              'Select a channel and paste the link here: ')
        write_file('slack_channel', slack_channel)
    print()
    return key, user_id, psw, project, slack_channel


key, user_id, psw, project, slack_channel = get_user_info()
email = user_id + '@holbertonschool.com'
user_data = {'api_key': key, 'email': email,
             'password': psw, 'scope': "checker"}
url = 'https://intranet.hbtn.io/users/auth_token.json'
auth = requests.post(url=url, data=user_data)
token = auth.json().get('auth_token')
if type(token) != str:
    print('Bad authentication (check your password and try again)')
    exit()

url_p = 'https://intranet.hbtn.io/projects/' + \
    project + '.json?auth_token=' + token
pj = requests.get(url=url_p)
print('requesting project info...')
i = 0
flag = 0
print('checking if checker will be available...')
while (i < len(pj.json().get('tasks'))):
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
    '''Sends requests for checker and notifies selected Slack channel'''
    url_request = 'https://intranet.hbtn.io/tasks/' + \
        str(task_id) + '/start_correction' + '.json?auth_token=' + str(token)
    request_dict = requests.post(url=url_request).json()
    request_id = request_dict.get('id')
    if request_id != 0:
        checkers = "Checker is out!"
        payload = {"text": checkers}
        requests.post(slack_channel, data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
        print('The checker is out and a message has been sent to Slack.')
        exit()
    else:
        checkers = 'Checker for ' + pj.json().get('name') + ' is not available'
        payload = {"text": checkers}
        requests.post(slack_channel, data=json.dumps(payload),
                      headers={'Content-Type': 'application/json'})
        from time import sleep
        sleep(10)

while (1):
    timed_job()
