import json
import urllib.request
import re
import matplotlib.pyplot as plt
from extra03.part2.helpers import FAILED_URL

ERRORS = ['Invalid\nlist', 'Invalid\nnumber', 'Result is a string,\nnot a number', 'Syntax\nerror']
count_errors = [0, 0, 0, 0]

# 6. Какие распространенные ошибки совершали студенты?
with urllib.request.urlopen(FAILED_URL) as url:
    failed = json.loads(url.read().decode())


def error_counter(lst):
    if lst[0] is None:
        count_errors[1] += 1
        return
    elif len(lst[0]) == 0:
        if re.match(r'^-?\d+(?:\.\d+)$', lst[1]):
            count_errors[1] += 1
        else:
            count_errors[0] += 1
    elif re.match(r'^-?\d+(?:\.\d+)$', lst[0]):
        count_errors[1] += 1
        return
    elif lst[0][0] == '[':
        count_errors[0] += 1
        return
    elif not re.sub(r'\'[\w]+\'', '', lst[0]):
        count_errors[2] += 1
        return
    elif re.sub(r'\'?(\s*[-+]?(\d+(?:\.\d*)?|\.\d+)([eE][-+]?\d+)?|[0x][\d]+\s*)\'?', '',
                lst[0]) == '' or lst[0][0] == '(' or lst[0] == 'None':
        count_errors[2] += 1
        return
    else:
        count_errors[3] += 1


for el in failed:
    error_counter(failed[el])

plt.title('Количество ошибок, которые совершали студенты')
plt.bar(ERRORS, count_errors)
plt.show()
