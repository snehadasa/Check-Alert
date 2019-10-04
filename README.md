# Checker Buddy
---
## This project makes use of Holberton School's Checker API.
The checker is a utility that runs a student's code against a test suite. It makes sure their code functions properly and even tests for edge cases.

![the checker](https://lh5.googleusercontent.com/AByTB2QIz3_JDrjs7LRuB4L-LxLb-1yjRjU8rzWfyR2UVKup7DYzPJXBCITHBcnW07axMVs0z4qgHoUyMSW2GBrnRxVpUhzja46SRhDjpEbcZUQwD2kFNMkkcBqi-hXVKNKJJDUX)

However, it is not immediately available to students when a new project is released. Sometimes it is withheld until an unspecified time to let students try to write functioning code without the additional assistance that the checker provides.

Wouldn't it be nice to know when the checker becomes available though? Some kind of an alert that lets you know you can check the code you've written? **Checker Buddy** uses Holberton's checker API to alert students when the checker is released. The alert is then sent to a Slack channel of their choice.

Occasionally a project does not have a checker. This may be because there needs to be a manual review by a human instead of an automatic review. In this case, **Checker Buddy** will let the student know that there will not be a checker for the specified project.

---
## How does it work?

To run this script, you'll first need to install **[APScheduler](https://apscheduler.readthedocs.io/en/latest/)**, a Python library that will periodically check to see if the checker is available.

To install **APScheduler** please use the following code:
`sudo pip3 install apscheduler `

Once you do that you'll be ready to clone this repo and run the script. You'll be met with a series of prompts that are necessary to make sure the correct project is being accessed. Here are the list of prompts you'll need to enter:
* Your API key from the '[My Tools](https://intranet.hbtn.io/dashboards/my_tools)' section of your Holberton profile
* Your Holberton School ID number
* Your Holberton School password (we do not store this password anywehre)
* The project ID, which can be found next to the project title on the project list page 

    * Find project ID:
       
        ![project_id](https://imgur.com/a/dVkilEd)
* URL for Slack channel to send alert to. Please visit the [Slack webhook website](https://checkalert.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks) to find this URL
---
### Demo of Usage
<!-- IMAGES OF USAGE --->

---
## About
### This project was created by:

* **David Kwan** - [GitHub](https://github.com/dwkwan) | [LinkedIn](https://www.linkedin.com/in/david-kwan-1b0930129/)
* **Marc Cavigli** - [GitHub](https://github.com/MCavigli) | [LinkedIn](https://www.linkedin.com/in/marccavigli/)
* **Sneha Dasa Lakshminath** - [GitHub](https://github.com/snehadasa) | [LinkedIn](https://www.linkedin.com/in/sneha-dasa-lakshmi\
nath-a3433539/)
* **Russell Molimock** - [GitHub](https://github.com/Rmolimock) | [LinkedIn](https://www.linkedin.com/in/russellmolimock/)
* **Thomas Graeff** - [GitHub](https://github.com/graefft) | [LinkedIn](https://www.linkedin.com/in/thomas-graeff-b3ab4380/)
* **Nick O'Keefe** - [GitHub](https://github.com/nokeefe) | [LinkedIn](https://www.linkedin.com/in/nbokeefe/)
* **Van Phan** - [GitHub](https://github.com/vdphan) | [LinkedIn](https://www.linkedin.com/in/van-phan-344764180/) 
At [Holberton School](http://holbertonschool.com).