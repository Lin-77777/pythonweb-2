#######################匯入模組#######################
import requests #匯入requests套件(用來發送請求)內建json模組
import os
import sys
#匯入ttkbootstrap模組，這是一個基於tkinter的第三方GUI框架，可以讓我們更輕鬆地創建美觀的GUI應用程式
from ttkbootstrap import *
#匯入PIL
from PIL import Image, ImageTk
#######################設定工作目錄########################
os.chdir(sys.path[0])#切換到當前腳本所在的目錄，這樣可以確保在執行腳本時，相關的文件和資源能夠正確地被找到和使用

#######################定義常數########################
API_KEY = "fec2377bf0b699adf269ea3d08bbe355"#API　KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"#API URL
UNITS = "metric"#單位，這裡設定為攝氏度
LANG = "zh_tw"#語言，這裡設定為中文
ICON_BASE_URL = "http://openweathermap.org/img/wn/"#天氣圖示URL

#######################定義函數########################
 
def on_switch_change():
    if  current_temperature==None:
           return
    if check_var.get() == True:
        label.config(text=f"溫度: {temp}°C")#將當前溫度顯示在標籤上
    else:
        label.config(text=f"溫度: {temp*1.8+32}°F")#將當前溫度顯示在標籤上 

def show_result():
    global current_temperature, weather_description, temp, desc#宣告全域變數，這樣在函數內部就可以修改這些變數的值了
    city_name = entry.get()#取得輸入框中的文字，這裡是要查詢的城市名稱
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
        temp = current_temperature#將當前溫度儲存在temp變數中，這樣就可以在後續的程式中使用這個變數來顯示溫度了
        desc = weather_description#將天氣描述儲存在desc變數中，這樣就可以在後續的程式中使用這個變數來顯示天氣描述了
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
    temp_image =f"{city_name}_weather_icon.png"
    
    on_switch_change()
    label2.config(text=f"天氣描述: {desc}")#將天氣描述顯示在標籤上
    image = Image.open(temp_image)
    #tkinter不能直接顯示PIL的Image物件，所以需要將其轉換為PhotoImage物件
    weather_photo = ImageTk.PhotoImage(image)
    label3.config(image=weather_photo)#將圖示保存成功的訊息顯示在標籤上
    label3.image =weather_photo #將圖示保存成功的訊息保存在標籤的image屬性中，這樣就不會被垃圾回收機制回收掉了，這樣圖示就可以正常顯示了


#######################建立視窗########################
window = Tk()#建立視窗
window.title("Checkbutton")#設定視窗標題
########################設定字型########################
font_size = 20 #設定字型大小
window.option_add("*Font", ("Helvetica",font_size))#設定視窗的字型，*Font是tkinter中的一個選項，用於設定所有元件的字型
#設定預設字型為Helvetica，大小為font_size
#######################設定主題########################
style = Style(theme="cyborg")#設定主題，Style是ttkbootstrap模組中的一個類別，用於設定主題，theme是要使用的主題名稱
style.configure("my.TButton", font=("Helvetica", font_size))#設定"my.TButton"的字型和顏色，font是字型
###########################建立輸入框########################
entry = Entry(window,width=30)#建立一個輸入框
entry.pack(padx=10, pady=10)#將輸入框加入主視窗，並設定輸入框的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)

#########################建立按鈕########################
button = Button(window, text="顯示天氣",command = show_result, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button.pack(padx=10, pady=10)#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
###########################建立文字框#########################
label = Label(window, text="溫度")#建立一個標籤，text是標籤上的文字
label.pack(padx=10, pady=10)#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
label2 = Label(window, text="形容")#建立一個標籤，text是標籤上的文字
label2.pack(padx=10, pady=10)#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
label3 = Label(window, text="圖示",image = None)#建立一個標籤，text是標籤上的文字
label3.pack(padx=10, pady=10)#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
######################建立變數########################
#建立一個BooleanVar變數，用於存儲Checkbutton的狀態
check_var = BooleanVar()#BooleanVar是tkinter模組中的一個類別，用於存儲布林值，這裡用它來存儲Checkbutton的狀態
#上面是設定為布林值變數，下面才是選定是True還是False
check_var.set(True)#將check_var的初始值設置為True，表示Checkbutton默認為選中狀態。

#####################建立勾勾########################
#Checkbutton=會和check_type綁在一起
#勾選時存True，取消勾選時存False，並存狀態改變時觸發 on_witch_change 函數
check = Checkbutton(window,
                    variable=check_var,
                    onvalue=True, 
                    offvalue=False,
                    command = on_switch_change,
                    style = "my.TCkeckbutton"
                    )
#建立一個Checkbutton，variable是Checkbutton綁定的變數，onvalue是勾選時存的值，offvalue是取消勾選時存的值，command是當Checkbutton狀態改變時要執行的函數，這裡使用lambda匿名函數來更新check_label的文字為check_var的當前值
#將 Checkbotton放到窗戶中的指定位置
check.pack( padx=10, pady=10)
#將Checkbutton加入主視窗，並設定Checkbutton的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)

#######################主程式########################
window.mainloop()#運行主事件循環，這樣視窗就會保持開啟狀態，直到用戶關閉它。


"""
from io import BytesIO
 Image.open(BytesIO(icon_response.content))#將下載的圖示內容轉換為PIL的Image物件，這樣就不需要先將圖示保存到本地了，可以直接在記憶體中處理圖示了
 photo = ImageTk.PhotoImage(image)#將PIL的Image物件轉換為PhotoImage物件，這樣就可以在tkinter中顯示圖示了
 image_label.config(image=photo)#將圖示顯示在標籤上
 image_label.image = photo#將圖示保存在標籤的image屬性中，這樣就不會被垃圾回收機制回收掉了，這樣圖示就可以正常顯示了
 """