import email.utils
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import datetime
from extra03.part2.helpers import MESSAGE_URL

# 1. Как по времени суток распределяется активность студентов?
# Наибольшая активность наблюдается с 12:00 по 23:00

with urllib.request.urlopen(MESSAGE_URL) as url:
    messages = json.loads(url.read().decode())
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

timed = []

for i in range(len(messages)):
    timed.append(datetime.datetime(1, 1, 1, messages[i][1][3], messages[i][1][4], messages[i][1][5]))
count = list(range(24))
for i in range(len(timed)):
    count[timed[i].time().hour] += 1

x = [datetime.datetime(2021, 3, 21) + datetime.timedelta(hours=i) for i in range(24)]
y = count

plt.plot(x, y)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
