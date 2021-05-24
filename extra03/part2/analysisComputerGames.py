import urllib.request
import re
import matplotlib.pyplot as plt

# 1. Какие годы были самыми популярными с точки зрения выхода игр? 1987-1997
# 2. Какие жанры были популярны в различные периоды времени? Arcade, Strategy
url = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'
resp = urllib.request.urlopen(url)
resp_data = resp.read()
data_str = str(resp_data.decode())
data_str = re.split(';|\n', data_str)

# Dates
dates = data_str[3::4]
set_dates = sorted(set(dates))
d_dates = dict.fromkeys(set_dates, 0)

for i in range(len(dates)):
    d_dates[dates[i]] += 1

# Genres
genres = data_str[1::4]
set_genres = sorted(set(genres))
d_genres = dict.fromkeys(set_genres, 0)
for i in range(len(genres)):
    d_genres[genres[i]] += 1

fig, axs = plt.subplots(2, figsize=(25, 10))
axs[0].bar(set_dates, list(d_dates.values()))
axs[1].bar(set_genres, list(d_genres.values()))
plt.show()
