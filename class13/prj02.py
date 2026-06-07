#######################模組#######################
import requests

#######################初始化#######################
API_KEY = "fec2377bf0b699adf269ea3d08bbe355"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
UNITS = "metric"
LANG = "zh_tw"
city_name = "Taipei"

send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
print(f"請求URL: {send_url}")

response = requests.get(send_url)
response.raise_for_status()  # 如果請求失敗，會丟出 HTTPError 異常，這樣就不會繼續執行後面的程式碼了
info = response.json()
#######################事件#######################
if "city" in info:
    for forecast in info.get("list"):
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        weather_description = forecast["weather"][0]["description"]
        print(dt_txt, temp, weather_description)
else:
    print(f"找不到城市: {city_name}")
#######################指令#######################

#######################啟動#######################


# 課堂小筆記
"""
變數名全大寫代表該變數的質不該被修改
"""
