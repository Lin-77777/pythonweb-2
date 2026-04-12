#######################匯入模組#######################
import requests #匯入requests套件(用來發送請求)內建json模組

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"#API　KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"#API URL
UNITS = "metric"#單位，這裡設定為攝氏度
LANG = "zh_tw"#語言，這裡設定為中文
#######################主程式########################
city_name = input("請輸入城市名稱: ")#讓使用者輸入城市名稱
#構成請求URL
send_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=" + UNITS + "&lang=" + LANG
print(f"請求URL: {send_url}")#印出請求URL，這樣可以檢查URL是否正確

response = requests.get(send_url)#發送請求，並將回應儲存在response變數中
infol  = response.json()#發送請求，並將回應儲存在response變數中
#&是URL參數的分隔符，q是要查詢的城市名稱，appid是API KEY，units是單位，lang是語言
