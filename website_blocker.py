""" This is a script that can be used as a Website Blocker 
to block access to given websites during certain interval in
a day """

# In order to run the python script as a service in background save the file 
# with extension ".pyw". Also you need to run the script as administrator.

# *** For Scheduling on Windows ***
# 1) Go to Task Scheduler
# 2) Create a Task -> Provide Name -> Configure for: Select the Windows Version 
# 3) Check the box to Run with highest privileges as we need administrator privileges
# 3) Triggers Tab -> Begin the Task: select At Startup for this script
# 4) Actions Tab -> for Action: Select Start a program -> Select the program from Browse


import time
from datetime import datetime as dt

# r is used to read the entered string ignoring all the special characters
#  such as \n etc...
host_path = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = "F:\\Udemy_Python\\website_blocker\hosts"
redirectIP = "127.0.0.1"
# list of websited to be blocked
website_list = ['www.facebook.com', 'facebook.com']

while True:
	# to check whether the current time is within 9 am and 5 pm
	if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
		with open(host_path, 'r+') as file:
			content = file.read()
			file.seek(0,2)
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirectIP + " " + website + "\n")
		file.close()
	else:
		with open(host_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()

# Script will check the time in an interval of 5 seconds
	time.sleep(5)