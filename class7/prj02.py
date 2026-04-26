######################匯入模組#######################
#匯入ttkbootstrap模組，這是一個基於tkinter的第三方GUI框架，可以讓我們更輕鬆地創建美觀的GUI應用程式
from ttkbootstrap import *
#匯入sys、os模組，用來設定工作目錄
import sys
import os
#匯入PIL
from PIL import Image, ImageTk
#####################設定工作目錄#####################
#將工作目錄切換到程式所在的目錄，這樣就可以直接使用相對路徑來讀取檔案了
os.chdir(sys.path[0])
#######################建立視窗########################
window = Tk()#建立視窗
window.title("Label_image")#設定視窗標題
######################讀取圖片########################
image = Image.open("image.png")
#tkinter不能直接顯示PIL的Image物件，所以需要將其轉換為PhotoImage物件
weather_photo = ImageTk.PhotoImage(image)
######################建立標籤########################
#label不只可以顯示文字，還可以顯示圖片，用法為:image=圖片物件
label = Label(window, image=weather_photo)#建立一個標籤，並將圖片物件指定給image參數，這樣標籤就會顯示圖片了
label.pack(padx=20,pady=20)#將標籤加入主視窗，並使用pack()方法來自動調整位置和大小
label.image = weather_photo#將圖片物件保存在標籤的image屬性中，這樣就不會被垃圾回收機制回收掉了，這樣圖片就可以正常顯示了
#######################運行應用程式########################
window.mainloop()#運行主事件循環，這樣視窗就會保持開啟狀態，直到用戶關閉它。