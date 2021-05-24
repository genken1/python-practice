MESSAGE_URL = 'https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json'
TABLE_URL = 'https://raw.githubusercontent.com/true-grue/kispython/main/pract3/table.json'
FAILED_URL = 'https://raw.githubusercontent.com/true-grue/kispython/main/pract3/failed.json'


def generate_groups():
    letter = ['К', 'В', 'М', 'Н']
    max_count = [25, 13, 2, 10]
    result = []
    for i in range(len(letter)):
        for j in range(max_count[i]):
            result.append(letter[i] + str(j + 1))
    return result
