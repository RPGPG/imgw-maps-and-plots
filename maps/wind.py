from PIL import Image, ImageFont, ImageDraw
import datetime
import json

src_file = open("/home/python-runner/data/twp.json", "r")
src_raw_json = src_file.read()
src = json.loads(src_raw_json)

font_color = (255, 255, 255)
font = ImageFont.truetype("/home/python-runner/maps/times.ttf", 20)

img_wind = Image.open("/home/python-runner/maps/mapa.png")
img_edit_wind = ImageDraw.Draw(img_wind)
font_wind = ImageFont.truetype("/home/python-runner/maps/times.ttf", 18)

# wiatr
img_edit_wind.text((370, 60), f"{src[5]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((131, 182), f"{src[47]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((400, 211), f"{src[53]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((782, 188), f"{src[0]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((663, 370), f"{src[55]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((314, 347), f"{src[37]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((126, 336), f"{src[6]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((134, 431), f"{src[61]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((525, 432), f"{src[27]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((798, 498), f"{src[25]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((257, 541), f"{src[28]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((627, 548), f"{src[13]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((450, 600), f"{src[11]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((752, 670), f"{src[41]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((577, 671), f"{src[19]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((634, 134), f"{src[31]['predkosc_wiatru']} m/s", font_color, font=font_wind)
img_edit_wind.text((355, 538), f"{src[32]['predkosc_wiatru']} m/s", font_color, font=font_wind)

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

img_edit_wind.text((16, 794), time, font_color, font=font)
img_edit_wind.text((16, 764), source, font_color, font=font)

img_wind.save("/home/python-runner/data/pics/maps/wind.png")
