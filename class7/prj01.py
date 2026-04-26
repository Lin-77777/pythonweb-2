



#######################匯入模組#######################
#匯入ttkbootstrap模組，這是一個基於tkinter的第三方GUI框架，可以讓我們更輕鬆地創建美觀的GUI應用程式
from ttkbootstrap import *
#匯入sys、os模組，用來設定工作目錄
import sys
import os
#####################設定工作目錄#####################
#將工作目錄切換到程式所在的目錄，這樣就可以直接使用相對路徑來讀取檔案了
os.chdir(sys.path[0])

#######################定義函數########################

def on_switch_change():
    check_label.config(text=str(check_var.get()))#當Checkbutton狀態改變時，更新check_label的文字為check_var的當前值
#######################建立視窗########################
window = Tk()#建立視窗
window.title("Checkbutton")#設定視窗標題
########################設定字型########################
font_size = 20 #設定字型大小
window.option_add("*Font", ("Helvetica",font_size))#設定視窗的字型，*Font是tkinter中的一個選項，用於設定所有元件的字型
#設定預設字型為Helvetica，大小為font_size
#######################設定主題########################
#設定主題樣式
style = Style(theme="cyborg")#設定主題，Style是ttkbootstrap模組中的一個類別，用於設定主題，theme是要使用的主題名稱
#設定按鈕與Checkbutton的字型樣式
style.configure("my.TButton", font=("Helvetica", font_size))#設定"my.TButton"的字型和顏色，font是字型
style.configure("my.TCheckButton", font=("Helvetica", font_size))#設定"my.TButton"的字型和顏色，font是字型


######################建立變數########################
#建立一個BooleanVar變數，用於存儲Checkbutton的狀態
check_var = BooleanVar()#BooleanVar是tkinter模組中的一個類別，用於存儲布林值，這裡用它來存儲Checkbutton的狀態
#上面是設定為布林值變數，下面才是選定是True還是False
check_var.set(True)#將check_var的初始值設置為True，表示Checkbutton默認為選中狀態。


####################建立標籤########################
check_label = Label(window, text="True")#建立一個標籤，text是標籤上的文字
check_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
#Checkbutton=會和check_type綁在一起
#勾選時存True，取消勾選時存False，並存狀態改變時觸發 on_witch_change 函數
check = Checkbutton(window,
                    variable=check_var,
                    onvalue=True, 
                    offvalue=False,
                    command = on_switch_change,
                    style = "my.TCkeckbutton"
                    )#建立一個Checkbutton，variable是Checkbutton綁定的變數，onvalue是勾選時存的值，offvalue是取消勾選時存的值，command是當Checkbutton狀態改變時要執行的函數，這裡使用lambda匿名函數來更新check_label的文字為check_var的當前值
#將 Checkbotton放到窗戶中的指定位置
check.grid(row=1, column=1, padx=10, pady=10, sticky="W")#將Checkbutton加入主視窗，並設定Checkbutton的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
#######################運行應用程式########################
window.mainloop()#運行主事件循環，這樣視窗就會保持開啟狀態，直到用戶關閉它。