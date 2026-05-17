################## 匯入模組 ##################
import requests  # 用來向天氣網站 (API) 發送 HTTP 請求，以獲取天氣資料

################# 定義類別 ##################
# 這份類別可以看成是把第一次實作天氣功能時的主程式流程拆開整理。
# 原本查天氣、取圖示代碼、取溫度、取描述等步驟都混在一起，現在把它們拆成一個個方法，
# 讓整體結構更清晰（物件導向），也更方便在其他專案重複使用。
# 現在改成「一個方法負責一件事」，比較容易看出每個功能在做的事。


class WeatherAPI:
    """把 OpenWeather 的查詢流程整理成可重複使用的工具類別"""

    def __init__(self, api_key, lang="zh_tw"):
        # __init__() 專門負責在建立物件時，初始化與準備共用設定。
        # 這樣就不用像早期那樣把所有設定都寫死在主程式裡，提升了彈性。

        self.api_key = api_key  # 儲存使用者的 OpenWeather API 授權金鑰 (API Key)
        self.units = "metric"  # 設定單位系統為公制 (metric)，確保回傳的溫度是攝氏 (°C) 而不是華氏或絕對溫度
        self.lang = lang  # 設定 API 回傳天氣描述的語言，預設為繁體中文 (zh_tw)

        # OpenWeather 取當前天氣資料的基礎 API 網址 (Endpoint)
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

        # OpenWeather 天氣圖示的基礎網址
        # 後續實作時，只需在網址後方拼接「圖示代碼@2x.png」即可取得對應天氣圖片 (例如 10d@2x.png)
        self.icon_url = "https://openweathermap.org/img/wn/"

    def get_weather(self, city):
        # 向天氣網站拿原始資料
        send_url = f"{self.base_url}&appid={self.api_key}&q={city}&units={self.units}&lang={self.lang}"

        response = requests.get(
            send_url
        )  # 發送 GET 請求到 OpenWeather API，並獲取回應物件
        return (
            response.json()
        )  # 將回應物件轉換為 JSON 格式的 Python 字典，並回傳給呼叫者

    def get_icon_url(self, icon_code):
        # 組合網址
        return f"{self.icon_base_url}{icon_code}@2x.png"


# 課堂小筆記
"""
有的時候格式化會自己家括號，沒有影響
"""
