import schedule
import time
import urllib.request
import json

def job():
	url ='https://www.reddit.com/r/all/top.json?t=hour&limit=3'
	jsonD = urllib.request.urlopen(url)
	jsonData = json.loads(jsonD.read())
	savefile=open('file.txt', 'a')
	for eachi in jsonData["data"]["children"]:
		savefile.write(str(eachi["data"]["title"] +"\n"))

	savefile.close()

schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1800) # wait 30 minutes
