from PIL import Image, ImageFont, ImageDraw
import datetime
import json

src_file = open("/home/python-runner/data/twp.json", "r")
src_raw_json = src_file.read()
src = json.loads(src_raw_json)

font_color = (255, 255, 255)
font = ImageFont.truetype("/home/python-runner/maps/times.ttf", 20)


img_pressure = Image.open("/home/python-runner/maps/mapa.png")
img_edit_pressure = ImageDraw.Draw(img_pressure)
font_pressure = ImageFont.truetype("/home/python-runner/maps/times.ttf", 13)

# cisnienie
img_edit_pressure.text((370, 60), f"{src[5]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((131, 182), f"{src[47]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((400, 211), f"{src[53]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((782, 188), f"{src[0]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((663, 370), f"{src[55]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((314, 347), f"{src[37]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((126, 336), f"{src[6]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((134, 431), f"{src[61]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((525, 432), f"{src[27]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((798, 498), f"{src[25]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((257, 541), f"{src[28]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((627, 548), f"{src[13]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((450, 600), f"{src[11]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((752, 670), f"{src[41]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((577, 671), f"{src[19]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((634, 134), f"{src[31]['cisnienie']} hPa", font_color, font=font_pressure)
img_edit_pressure.text((355, 538), f"{src[32]['cisnienie']} hPa", font_color, font=font_pressure)

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

img_edit_pressure.text((16, 794), time, font_color, font=font)
img_edit_pressure.text((16, 764), source, font_color, font=font)

img_pressure.save("/home/python-runner/data/pics/maps/pressure.png")
