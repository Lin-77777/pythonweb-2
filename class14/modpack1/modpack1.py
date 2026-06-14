################## 匯入模組 ##################
import requests  # 用來向天氣網站 (API) 發送 HTTP 請求，以獲取天氣資料
import openai #匯入openai模組
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
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast?"

        # OpenWeather 天氣圖示的基礎網址
        # 後續實作時，只需在網址後方拼接「圖示代碼@2x.png」即可取得對應天氣圖片 (例如 10d@2x.png)
        self.icon_base_url = "https://openweathermap.org/img/wn/"

    def get_current_weather(self, city):
        # 向天氣網站拿原始資料
        send_url = f"{self.base_url}appid={self.api_key}&q={city}&units={self.units}&lang={self.lang}"

        response = requests.get(
            send_url
        )  # 發送 GET 請求到 OpenWeather API，並獲取回應物件
        return (
            response.json()
        )  # 將回應物件轉換為 JSON 格式的 Python 字典，並回傳給呼叫者

    def get_icon_url(self, icon_code):
        # 組合網址
        return f"{self.icon_base_url}{icon_code}@2x.png"

    def get_weather_summary(self, city_name):
        """查詢目前天氣，並整理成更容易使用的摘要資料。"""
        # 這裡把原本較完整的 API 資料，整理成比較好閱讀的天氣小抄。
        # 和第一次直接在主程式裡拆資料相比，這一步多做了「資料整理」的功能分割：
        # 主程式之後只要拿整理好的結果來用，就不用每次自己拆很多層字典。
        info = self.get_current_weather(city_name)
        print(info)  # 可以先印出原始資料，看看裡面有哪些欄位，方便後續整理成摘要
        if "weather" in info and "main" in info:
            return {
                "city_name": info.get("name", city_name),
                # 優先使用 API 回傳的正式城市名稱
                "temperature_celsius": round(info["main"]["temp"], 2),
                # 把攝氏溫度整理成小數點 2 位
                "description": info["weather"][0]["description"],
                # 天氣描述文字，例如多雲、陰天
                "icon_code": info["weather"][0]["icon"],
                # 天氣圖示代碼，之後可以再組成圖片網址
            }

        return None  # 如果沒有拿到主要天氣資料，就回傳 None

    def get_icon(self, icon_code):
        # 這個方法和第一次實作時下載圖示的那一段最接近。
        # 差別是現在把流程拆成兩小步：
        # 1. get_icon_url() 先負責組圖示網址
        # 2. get_icon() 再負責把圖片原始資料抓回來
        # 這樣學生會比較容易看出「組網址」和「下載資料」是兩個不同工作。
        icon_url = self.get_icon_url(icon_code)
        response = requests.get(icon_url)
        if response.status_code == 200:
            return response.content  # content 裡放的是圖片的原始資料
        return None

    def get_forecast(self, city_name):
        # get_forecast() 的實作和 get_current_weather() 非常類似，差別在於它使用了不同的 API 網址 (forecast_url)，
        # 都是先組合好請求網址，然後發送 GET 請求，最後把回應轉換成 JSON 格式的字典回傳給呼叫者。
        # 但是是在可以變成三小時拿一筆
        send_url = f"{self.forecast_url}appid={self.api_key}&q={city_name}&units={self.units}&lang={self.lang}"
        response = requests.get(send_url)
        return response.json()

    def get_forecast_summary(self, city_name, count=10):
        """查詢未來天氣預報，並整理成更容易使用的摘要資料。"""
        # 這裡和 get_weather_summary() 類似
        # 先把API回傳的原始資料整理好，再回傳給主程式使用
        # 這樣Discord Bot 或GUI就不用每次自己拆很多層字典了
        forecast_count = max(0, count)  # 確保 count 不會是負數
        try:
            info = self.get_forecast(city_name)
        except requests.HTTPError as error:
            response = error.response
            if response is not None and response.status_code == 404:
                return None  # 如果請求失敗，回傳 None
            raise  # 在程式暫停的狀況下，回報錯誤

        if "city" not in info or "list" not in info:
            return None  # 如果沒有拿到主要天氣資料，就回傳 None

        city_label = info["city"].get("name", city_name)
        forecast_summary = []

        for forecast in info["list"][
            :forecast_count
        ]:  # 這裡的冒號是從0開始的簡化，原本完整程式碼為[0:forecast_count]
            forecast_summary.append(
                {
                    "city_name": city_label,
                    "datetime": forecast.get("dt_txt"),
                    "temperature_celsius": round(forecast["main"]["temp"], 2),
                    "description": forecast["weather"][0]["description"],
                    "icon_code": forecast["weather"][0]["icon"],
                }
            )
        return forecast_summary
class AIAssisant:
    #__init__()負責準備OpenAI的設定
    #把API金鑰存起來,之後才能用來呼叫OpenAI的服務
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key
    def ask(self,system_propmt,user_message,history_messages=None,temperture=0.1,model="gpt-4o"):
        """進行一次AI對話，適合完成單次任務，例如分析天氣預報資料。"""
        #這個方法可以讓我們可以問AI一個問題，並得到一次性的回答。
        #system_propmt是給AI的角色設定，告訴AI它是誰，要做什麼任務
        #user_message是我們要問AI的問題或提供給AI的資料
        #history_messages是之前的對話紀錄，如果有的話可以讓AI參考，讓回答更連貫

        #如果沒有設定金鑰，直接回傳錯誤訊息
        if not self.api_key:
            return None,"尚未設定 OpenAI API 金鑰，請先在 .env 檔案中完成設定。"
      
        if history_messages is None:  
            history_messages = []  # 如果沒有提供歷史訊息，就用空列表代替，#這兩行的用意是防止在下方加法的地方error
        #messages的順序很重要:
        #1. system:先告訴AI它是誰，要做什麼任務
        #2. user:再提供AI需要分析的資料或問題
        #3.history:放入已經整理好的舊對話
        #4.user:最後放這次真正要問的新問題
        messages = (
            [{"role": "system", "content": system_propmt}]
            + history_messages
            + [{"role": "user", "content": user_message}]
        )
        print("=== 傳給 OpenAI 的訊息 ===")
        for msg in messages:
            print(f"{msg['role']}: {msg['content']}")
        print("===========================")
        try:
            #向OpenAI發送請求
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperture,
            )
            #取出AI的回答
            assistant_message = response.choices[0].message.content
            
            return assistant_message,None#成功時回傳回答，錯誤訊息為None
        
        except Exception as e:
            #如果OpenAI回傳錯誤，回傳錯誤訊息
            return None,f"發生錯誤: {e}"
# 課堂小筆記
"""
有的時候格式化會自己家括號，沒有影響
 raise在程式暫停的狀況下，回報錯誤
"""
