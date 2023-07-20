import gspread
gc = gspread.oauth(credentials_filename='/home/pi/Desktop/WeatherStation/Adafruit_Python_DHT/examples/credentials.json')
sh = gc.open("DHT Humidity Logs")
print(sh.sheet1.get('A1'))