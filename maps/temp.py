from PIL import Image, ImageFont, ImageDraw
import datetime
import json

src_file = open("/home/python-runner/data/twp.json", "r")
src_raw_json = src_file.read()
src = json.loads(src_raw_json)

img = Image.open("/home/python-runner/maps/mapa.png")
img_edit = ImageDraw.Draw(img)
font = ImageFont.truetype("/home/python-runner/maps/times.ttf", 20)

font_color = (255, 255, 255)

# Gdańsk 5
img_edit.text((370, 60), f"{src[5]['temperatura']}℃", font_color, font=font)
# Szczecin 47
img_edit.text((131, 182), f"{src[47]['temperatura']}℃", font_color, font=font)
# Toruń 53
img_edit.text((400, 211), f"{src[53]['temperatura']}℃", font_color, font=font)
# Białystok 0
img_edit.text((782, 188), f"{src[0]['temperatura']}℃", font_color, font=font)
# Warszawa 55
img_edit.text((663, 370), f"{src[55]['temperatura']}℃", font_color, font=font)
# Poznań 37
img_edit.text((314, 347), f"{src[37]['temperatura']}℃", font_color, font=font)
# Gorzów 6
img_edit.text((126, 336), f"{src[6]['temperatura']}℃", font_color, font=font)
# Zielona Góra 61
img_edit.text((134, 431), f"{src[61]['temperatura']}℃", font_color, font=font)
# Łódź 27
img_edit.text((525, 432), f"{src[27]['temperatura']}℃", font_color, font=font)
# Lublin 25
img_edit.text((798, 498), f"{src[25]['temperatura']}℃", font_color, font=font)
# Wrocław 28
img_edit.text((257, 541), f"{src[28]['temperatura']}℃", font_color, font=font)
# Kielce 13
img_edit.text((627, 548), f"{src[13]['temperatura']}℃", font_color, font=font)
# Katowice 11
img_edit.text((450, 600), f"{src[11]['temperatura']}℃", font_color, font=font)
# Rzeszów 41
img_edit.text((752, 670), f"{src[41]['temperatura']}℃", font_color, font=font)
# Kraków 19
img_edit.text((577, 671), f"{src[19]['temperatura']}℃", font_color, font=font)
# Olsztyn 31
img_edit.text((634, 134), f"{src[31]['temperatura']}℃", font_color, font=font)
# Opole 32
img_edit.text((355, 538), f"{src[32]['temperatura']}℃", font_color, font=font)

time = datetime.datetime.now()
day = time.day
month = time.month
year = time.year
hour = time.hour
minute = time.minute
source = "danepubliczne.imgw.pl"
if len(str(month)) == 1:
    month = f"0{month}"
if len(str(day)) == 1:
    day = f"0{day}"
if len(str(hour)) == 1:
    hour = f"0{hour}"
if len(str(minute)) == 1:
    minute = f"0{minute}"

time = f"{day}.{month}.{year} {hour}:{minute}"
img_edit.text((16, 794), time, font_color, font=font)
img_edit.text((16, 764), source, font_color, font=font)

img.save("/home/python-runner/data/pics/maps/temp.png")
