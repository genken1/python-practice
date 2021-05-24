import email.utils
import json
import urllib.request
import matplotlib.pyplot as plt

# 5. Какие задачи оказались самыми легкими, самыми сложными?
from extra03.part2.helpers import TABLE_URL, MESSAGE_URL


def generate_tasks():
    letter = 'f'
    max_count = [4, 3, 2]
    result = []
    for i in range(len(max_count)):
        for j in range(max_count[i]):
            result.append(letter + str(i + 1) + str(j + 1))
    return result


def div(ones, zeros):
    result = []
    for i in range(len(ones)):
        print(ones[i], zeros[i])
        try:
            result.append(ones[i] / (ones[i] + zeros[i]))
        except ZeroDivisionError:
            result.append(0)
    return result


with urllib.request.urlopen(TABLE_URL) as url:
    table = json.loads(url.read().decode())
with urllib.request.urlopen(MESSAGE_URL) as url:
    messages = json.loads(url.read().decode())
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

dZero = dict.fromkeys(generate_tasks(), 0)
dOne = dict.fromkeys(generate_tasks(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    key = table['data'][i][2]
    if score == 0:
        dZero[key] += 1
    else:
        dOne[key] += 1
x = generate_tasks()
y = div(list(dOne.values()), list(dZero.values()))
plt.subplots()
plt.title('Отношение 1-иц к общему количеству попыток за задания')
plt.bar(x, y)
plt.show()
