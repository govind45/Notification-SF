import json
from datetime import datetime
import requests
import base64

headers = {'Authorization': 'token 76b529dc05684356b4593cab9eaae569b9dea940'}
schedule_url = "https://git.soma.salesforce.com/api/v3/repos/iaas/private-cloud-patch-scheduler/contents/schedule/patching-schedule.json"
schedule_text = requests.get(schedule_url, headers=headers)
schedule_json = schedule_text.json()
schedule_json = schedule_json['content']
schedule_json = base64.b64decode(schedule_json)
schedule_json = schedule_json.decode('utf-8')
schedule_json = json.loads(schedule_json)
schedule_date = schedule_json["schedule"]["start_date"]
print (schedule_date)
today_date = datetime.now()
today_date_string = today_date.strftime("%Y")+'-'+today_date.strftime("%m")+'-'+today_date.strftime("%d")
print (today_date_string)
today_date_final = datetime.strptime(today_date_string, "%Y-%m-%d")
schedule_date_final = datetime.strptime(schedule_date, "%Y-%m-%d")
num_of_days_due = (schedule_date_final-today_date_final).days
print (num_of_days_due)

if num_of_days_due == 7:
	notification = True
else:
	notification = False

try:
	print (notification)
except Exception as e:
	print ("exiting..")