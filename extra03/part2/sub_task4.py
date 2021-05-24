import json
import urllib.request
import matplotlib.pyplot as plt
from extra03.part2.helpers import generate_groups, MESSAGE_URL

# 4. В каких группах было получено больше всего правильных решений?
# К1, В7, К6
with urllib.request.urlopen(MESSAGE_URL) as url:
    table = json.loads(url.read().decode())

d = dict.fromkeys(generate_groups(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    if score == 1:
        key = table['data'][i][0]
        d[key] += 1
x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20, 10))
plt.bar(x, y)
plt.show()
