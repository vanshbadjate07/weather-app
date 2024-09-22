#Weather app where we can see temperature in celcious of entered city!!
import requests
import json
import os

city=input("Enter name of City\n")

url=f"https://api.weatherapi.com/v1/current.json?key=e216b0ab726d4674bd790044242209&q={city}"

r=requests.get(url)
d=json.loads(r.text)

print(f"Temperatur of {city} in Celcious {d["current"]["temp_c"]}")
print(f"Temperatur of {city} in Fahrenheit {d["current"]["temp_f"]}")

text1=f"say Temperature of {city} in Celcious is {d["current"]["temp_c"]}"
text2=f"say Temperature of {city} in Fahrenhite is {d["current"]["temp_f"]}"

os.system(text1)
os.system(text2)