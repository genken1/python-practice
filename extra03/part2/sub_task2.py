import json
import urllib.request
import matplotlib.pyplot as plt
from extra03.part2.helpers import MESSAGE_URL

# 2. Как по дням недели распределяется активность студентов?
# Видно из графика

with urllib.request.urlopen(MESSAGE_URL) as url:
    messages = json.loads(url.read().decode())

check = list(range(7))
for i in range(len(messages)):
    week_day = messages[i]['date'][:3]
    if week_day == 'Mon':
        check[0] += 1
    elif week_day == 'Tue':
        check[1] += 1
    elif week_day == 'Wed':
        check[2] += 1
    elif week_day == 'Thu':
        check[3] += 1
    elif week_day == 'Fri':
        check[4] += 1
    elif week_day == 'Sat':
        check[5] += 1
    elif week_day == 'Sun':
        check[6] += 1

week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x = week_days
y = check
plt.subplots()
plt.bar(x, y)
plt.show()
