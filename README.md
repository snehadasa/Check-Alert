# ![logo](https://i.imgur.com/kRERWFj.png) Check Alert
---
## This project makes use of Holberton School's Checker API.
The checker is a utility that runs a student's code against a test suite. It makes sure their code functions properly and even tests for edge cases.

![the checker](https://lh5.googleusercontent.com/AByTB2QIz3_JDrjs7LRuB4L-LxLb-1yjRjU8rzWfyR2UVKup7DYzPJXBCITHBcnW07axMVs0z4qgHoUyMSW2GBrnRxVpUhzja46SRhDjpEbcZUQwD2kFNMkkcBqi-hXVKNKJJDUX)

However, it is not immediately available to students when a new project is released. Sometimes it is withheld until an unspecified time to let students try to write functioning code without the additional assistance that the checker provides.

Wouldn't it be nice to know when the checker becomes available though? Some kind of an alert that lets you know you can check the code you've written? **Check Alert** uses Holberton's checker API to alert students when the checker is released. The alert is then sent to a Slack channel of their choice.

Occasionally a project does not have a checker. This may be because there needs to be a manual review by a human instead of an automatic review. In this case, **Check Alert** will let the student know that there will not be a checker for the specified project.

---
## How does it work?

First you'll need to `git clone` this repository so you have the script. Please enter the following command:

`git clone https://github.com/nokeefe/Check-Alert.git`

When you run the script, you'll be met with a series of prompts that are necessary to make sure the correct project is being accessed. Here are the list of prompts you'll need to enter:
* Your API key from the '[My Tools](https://intranet.hbtn.io/dashboards/my_tools)' section of your Holberton profile. Click the link and scroll to the bottom of the page.
* Your Holberton School ID number.
* Your Holberton School password (we do not store this password anywehre).
* The project ID, which can be found next to the project title on the project list page.

   ![project_id](https://i.imgur.com/m6BYfFU.png?1)

* URL for Slack channel to send alert to. Please visit the [Slack webhook website](https://checkalert.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks) to find this URL

    ![webhook](https://i.imgur.com/ulj2AQ7.png)
---
## Demo of Usage

```
Check-Alert$ ./check_alert.py

Visit: https://intranet.hbtn.io/dashboards/my_tools
and enter your API key from the bottom of the page:
<Your API key>

Enter your Holberton ID:
<Your Holberton ID>

Enter your Holberton password. (We do not store it)
<Your Holberton password>

Which project? (ID at the end of the project's URL)
<The project ID>

Please visit https://checkalert.slack.com/apps/new/A0F7XDUAZ-incoming-webhooks
Select a channel and paste the link here:
<Long link>
```

---
## About
### This project was created by:

* **David Kwan** - [GitHub](https://github.com/dwkwan) | [LinkedIn](https://www.linkedin.com/in/david-kwan-1b0930129/)
* **Marc Cavigli** - [GitHub](https://github.com/MCavigli) | [LinkedIn](https://www.linkedin.com/in/marccavigli/)
* **Sneha Dasa Lakshminath** - [GitHub](https://github.com/snehadasa) | [LinkedIn](https://www.linkedin.com/in/sneha-dasa-lakshminath-a3433539/)
* **Russell Molimock** - [GitHub](https://github.com/Rmolimock) | [LinkedIn](https://www.linkedin.com/in/russellmolimock/)
* **Thomas Graeff** - [GitHub](https://github.com/graefft) | [LinkedIn](https://www.linkedin.com/in/thomas-graeff-b3ab4380/)
* **Nick O'Keefe** - [GitHub](https://github.com/nokeefe) | [LinkedIn](https://www.linkedin.com/in/nbokeefe/)
* **Van Phan** - [GitHub](https://github.com/vdphan) | [LinkedIn](https://www.linkedin.com/in/van-phan-344764180/) 
at [Holberton School](http://holbertonschool.com)
