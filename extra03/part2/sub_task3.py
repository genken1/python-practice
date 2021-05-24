import email.utils
import json
import urllib.request
import matplotlib.pyplot as plt
from extra03.part2.helpers import generate_groups, MESSAGE_URL

# 3. В каких группах было отправлено больше всего сообщений?
# В7, К13, Н5
with urllib.request.urlopen(MESSAGE_URL) as url:
    messages = json.loads(url.read().decode())

messagesArr = []
for m in messages:
    messagesArr.append((m['subj'].upper(), email.utils.parsedate(m['date'])))

d = dict.fromkeys(generate_groups(), 0)
for i in range(len(messagesArr)):
    key = messagesArr[i][0].split()[0].upper()
    d[key] += 1

x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20, 10))
plt.bar(x, y)
plt.show()
