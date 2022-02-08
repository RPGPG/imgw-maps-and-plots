import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime
import json


def draw_plot(city_name, city_html_code):
    src_file = open("/home/python-runner/data/twp.json", "r")
    src_raw_json = src_file.read()
    src = json.loads(src_raw_json)
    temp_now = src[int(city_html_code)]["temperatura"]
    try:
        file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", "a")
        file.write(f"\n{temp_now}")
        if len(temp_now) == 0:
            exit()
    finally:
        file.close()

    needTrim = False

    # sprawdzenie czy jest ponad 24 wartosci w pliku
    try:
        file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", "r")
        count = 0
        for line in file:
            count += 1
        if count > 24:
            needTrim = True
    finally:
        file.close()

    # jesli jest, to ucinanie najstarszych wartosci
    if needTrim:
        try:
            file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", "r")
            temps = []
            for line in file:
                temps.append(line)
            while len(temps) > 24:
                temps.pop(0)
        finally:
            file.close()

        # czyszczenie pliku i wklejanie wartosci z tablicy temps
        try:
            file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", 'r+')
            file.truncate(0)
            file.close()
            file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", "a")
            for num in temps:
                file.write(str(num))
        finally:
            file.close()

    # rysowanie wykresu
    try:
        file = open(f"/home/python-runner/data/pics/plots/raw_data/{city_name}", "r")
        temps = []
        for line in file:
            temps.append(float(line))
        min_val = min(temps)
        max_val = max(temps)
        if max_val - min_val > 10:
            tick = 1
        else:
            tick = 0.5
    finally:
        file.close()
        time = datetime.datetime.now()
        hour = time.hour
        minute = time.minute
        if minute < 15:
            if hour == 0:
                hour = 23
            else:
                hour -= 1
        hours = []
        for i in range(24):
            hours.append(hour)
            if hour == 0:
                hour = 23
            else:
                hour -= 1
        xhours = []
        for i in hours:
            xhours.append(str(i))
        xhours.reverse()

        COLOR = 'white'
        mpl.rcParams['text.color'] = COLOR
        mpl.rcParams['axes.labelcolor'] = COLOR
        mpl.rcParams['xtick.color'] = COLOR
        mpl.rcParams['ytick.color'] = COLOR

        fig = plt.figure(figsize=(12.0, 6.0))

        fig.patch.set_facecolor("#0f202b")

        plt.plot(xhours, temps)
        plt.vlines(xhours, min_val, temps, linestyles="dashed")
        plt.ylabel("℃")
        plt.xlabel("Godz.")
        plt.xticks(xhours)
        plt.yticks(np.arange(min_val, max_val + 1, tick))
        ax = plt.gca()
        ax.set_facecolor("#081721")

        plt.savefig(f"/home/python-runner/data/pics/plots/{city_name}_plot.png")


# dict z miastami i kodami
cities = {
    "gdansk": "5",
    "szczecin": "47",
    "torun": "53",
    "bialystok": "0",
    "warszawa": "55",
    "poznan": "37",
    "gorzow": "6",
    "zielona_gora": "61",
    "lodz": "27",
    "lublin": "25",
    "wroclaw": "28",
    "kielce": "13",
    "katowice": "11",
    "rzeszow": "41",
    "krakow": "19",
    "olsztyn": "31",
    "opole": "32"
}

for key in cities:
    draw_plot(key, cities[key])
