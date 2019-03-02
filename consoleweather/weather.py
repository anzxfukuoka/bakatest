import requests
import json
import consoleweather.config as conf
from consoleweather.icons import *

def get_weather(city = "Kiev", units = "metric"):

	re = ""

	try:
		res = requests.get("http://api.openweathermap.org/data/2.5/find",
	                 params={'q': city, "units": units ,"lang": conf.lang,'APPID': conf.appid})

		data = res.json()
		#print(json.dumps(data, indent=4, sort_keys=True))

		re += str(int(data['list'][0]['main']["temp"])) + "°C" + "\n"
		re += data['list'][0]["weather"][0]['description'] + "\n"

		#print("восход: ", int(data['list'][0]['sys']["sunrise"]))
		#print("закат: ", int(data['list'][0]['sys']["sunset"]))

		ic = data['list'][0]["weather"][0]['icon']

		if(ic == "01d"):
			re += icon["sun"] + "\n"
		if(ic == "01n"):
			re += icon["moon"] + "\n"
		if(ic == "02d"):
			re += icon["sun_cloud"] + "\n"
		if(ic == "02n"):
			re += icon["moon_cloud"] + "\n"
		if(ic == "03d" or ic == "03n"
		 or ic == "04d" or ic == "04n"):
			re += icon["cloud"] + "\n"
		if(ic == "09d" or ic == "09n"):
			re += icon["cloud"] + "\n"
			re += icon["rain"] + "\n"
		if(ic == "10d"):
			re += icon["sun_cloud"] + "\n"
			re += icon["rain"] + "\n"
		if(ic == "10n"):
			re += icon["moon_cloud"] + "\n"
			re += icon["rain"] + "\n"
		if(ic == "11d"):
			re += icon["sun_cloud"] + "\n"
			re += icon["thunder"] + "\n"
		if(ic == "11n"):
			re += icon["moon_cloud"] + "\n"
			re += icon["thunder"] + "\n"
		if(ic == "13d" or ic == "13n"):
			re += icon["cloud"] + "\n"
			re += icon["snow"] + "\n"
		if(ic == "50d" or ic == "50n"):
			re += icon["cloud"] + "\n"
			re += icon["fog"] + "\n"


		re += "давление: " + str(int(data['list'][0]['main']["pressure"]) * 0.75) + "мм рт.ст." + "\n"
		re += "влажность: " + str(int(data['list'][0]['main']["humidity"])) + "%" + "\n"
		re += "ветер: " + str(int(data['list'][0]['wind']["speed"])) + "м/с"

	except Exception as e:
		print("err:",e)
		pass
	finally:
		return re

#print(get_weather())
