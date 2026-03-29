#######################匯入模組#######################
#匯入ttkbootstrap模組
#pip install ttkbootstrap -U(安裝ttkbootstrap模組，這是一個基於tkinter的主題庫，可以讓你的tkinter應用程式看起來更美觀)
from ttkbootstrap import *#以內建tkinter
#先安裝Pillow模組(pip install pillow)，然後再匯入Image和ImageTk模組
import sys
import os
"""
*表示匯入模組中的所有函數和物件(這樣就可以直接使用tkinter中的函數和物件，
而不需要每次都寫tkinter.指令)
"""

#######################定義函數########################
def test():
    print("114514")
#######################建立視窗########################
window = Tk()#Tk()是tkinter模組中的一個物件，用於創建主視窗對象。當你調用Tk()時，它會創建一個新的主視窗。
window.title("我的第一個GUI應用程式")#設定視窗標題

#######################設定字型########################
font_size = 12#設定字型大小
window.option_add("*Font", ("Helvetica",font_size))#設定視窗的字型，*Font是tkinter中的一個選項，用於設定所有元件的字型

#######################設定主題########################
style = Style(theme="cyborg")#設定主題，Style是ttkbootstrap模組中的一個類別，用於設定主題，theme是要使用的主題名稱
# "my.TButton"的命名邏輯:
#就像幫東西貼標籤一樣，分成兩個部分，用"."隔開:
#     前半段 "my"   ->自己取的名字，例如"big"、"red"
#     後半段 "TButton" ->固定寫法，代表"按鈕"這種元件
#                        T是Ttk(一種按鈕工具箱)的縮寫
#                        就像"衣服"的T一樣，是品牌名稱的開頭
#常見元件的後半段寫法:
#     按鈕 -> TButton
#     標籤 -> TLabel
#     輸入框 -> TEntry
style.configure("my.TButton", font=("Helvetica", font_size))#設定"my.TButton"的字型和顏色，font是字型
#######################建立標籤########################
label = Label(window, text="114514")#建立一個標籤，text是標籤上的文字
label.grid(row=0, column=0, padx=10, pady=10,sticky="E")#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
#######################建立按鈕########################

button = Button(window, text="按我顯示114514",command = test, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button.grid(row=0, column=1, padx=10, pady=10,sticky="W")#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
button2 = Button(window, text="Click Me to desplay 114514",command = test, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button2.grid(row=1, column=0, columnspan=2,padx=10, pady=10,sticky="EW")#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
"""
columnspan是讓直的融合(看起來是橫的變大)，rowspan是讓橫的融合(看起來直的變大)
columnspan要包含自己的位置，所以要增加的話至少要2
"""
######################運行應用程式########################
window.mainloop()#運行主事件循環，這樣視窗就會保持開啟狀態，直到用戶關閉它。
#課堂小筆記
#下面多行註解前面加了r，讓所有東西都變成真正的純文字(原始字符串)。
r'''
物件才會###.####()
物件跟類別是同一個意思
指令()會直接執行，而指令不加()則是將函數本身作為一個物件傳遞，這樣就可以在需要的時候找它。
在planmode中可以用請提出計畫讓ai這樣就可以檢查計畫是符合你的需求
c.get是config.get的簡寫，這樣就可以直接使用c.get()來獲取元件c的屬性值，例:c.get("text")可以獲取元件c的text屬性值。
### = not (###)是將變數###的值取反，如果###是True，則變為False；如果###是False，則變為True。
顏色編碼#RRGGBB
RR是紅色的值，GG是綠色的值，BB是藍色的值，每個值都是從00到FF的十六進制數字，表示顏色的強度。FF是255的十六進制表示，表示顏色的最大強度；00表示顏色的最小強度
絕對路徑是從根目錄(c巢)開始的路徑，例如C:\Users\Username\Documents\file.txt
在寫程式時可以用sys.path[0]找到現在寫此程式的檔案所屬的資料夾，這樣就可以讀取同一個資料夾中的其他檔案，例如圖片檔案，這樣就不需要寫絕對路徑了。
python座標系統是以左上角為原點(0,0)，x軸向右增加，y軸向下增加，負數則在視窗外。
數學座標則是以左下角為原點(0,0)，x軸向右增加，y軸向上增加。
row=橫排
column=直排
grid=網格(大小會因內容改變)
'''