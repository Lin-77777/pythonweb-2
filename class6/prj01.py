#######################匯入模組#######################
import requests #匯入requests套件(用來發送請求)內建json模組
import os
import sys
#######################定義常數########################
API_KEY = "fec2377bf0b699adf269ea3d08bbe355"#API　KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"#API URL
UNITS = "metric"#單位，這裡設定為攝氏度
LANG = "zh_tw"#語言，這裡設定為中文
ICON_BASE_URL = "http://openweathermap.org/img/wn/"#天氣圖示URL

#######################主程式########################
os.chdir(sys.path[0])#切換到當前腳本所在的目錄，這樣可以確保在執行腳本時，相關的文件和資源能夠正確地被找到和使用

city_name = input("請輸入城市名稱: ")#讓使用者輸入城市名稱
#構成請求URL
send_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=" + UNITS + "&lang=" + LANG
print(f"請求URL: {send_url}")#印出請求URL，這樣可以檢查URL是否正確

response = requests.get(send_url)#發送請求，並將回應儲存在response變數中，requests是模組
info = response.json()#發送請求，並將回應儲存在response變數中
#&是URL參數的分隔符，q是要查詢的城市名稱，appid是API KEY，units是單位，lang是語言

#處理和顯示天氣資訊
if not (info.get("cod")=="404"):#如果回應的狀態碼不是404，表示找到城市
    current_temperature = info["main"]["temp"]#從回應中提取當前溫度
    weather_description = info["weather"][0]["description"]#從回應中提取天氣描述
    icon_code = info["weather"][0]["icon"]#從回應中提取天氣圖示代碼
    """
    info["weather"]是一個字典的key所以拿到的是裡面的值，是一個list，
    所以要用[0]來取得list中的第一個元素，這個元素是一個字典的key，所以用["icon"]來取得圖示代碼
    """
    print(f"{city_name}的當前溫度: {current_temperature}°C")#印出當前溫度
    print(f"{city_name}的天氣描述: {weather_description}")#印出天氣描述

    #根據圖標代碼組成圖標下載URL
    icon_url = f"{ICON_BASE_URL}{icon_code}@4x.png"

    #下載圖標並保存到本地
    print(f"下載天氣圖示: {icon_url}")#印出圖示URL
    icon_response = requests.get(icon_url)#發送請求下載圖示
    #若下載成功，則將圖示保存成png檔
    if icon_response.status_code == 200:
        #with open(...,"wb")的意思是:
        #with 會在程式離開with區塊時自動關閉檔案，"wb"表示以二進位寫入模式打開檔案，這樣可以確保圖示能夠正確地保存到本地
        
        with open(f"{city_name}_weather_icon.png","wb") as icon_file:
            icon_file.write(icon_response.content)#將下載的圖示內容寫入檔案
        print(f"天氣圖示已保存為: {city_name}_weather_icon.png")#印出圖示保存成功的訊息
    else:
        print(f"無法下載天氣圖示，HTTP狀態碼: {icon_response.status_code}")#如果下載圖示失敗，印出錯誤訊息和HTTP狀態碼
else:
    print(f"找不到城市: {city_name}")#如果回應的狀態碼是404，表示找不到城市，印出錯誤訊息




#課堂筆記

"""
在網址後的?後面是參數，參數之間用&分隔，參數的格式是key=value
"""