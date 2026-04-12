#######################匯入模組#######################
#匯入ttkbootstrap模組
#pip install ttkbootstrap -U(安裝ttkbootstrap模組，這是一個基於tkinter的主題庫，可以讓你的tkinter應用程式看起來更美觀)
from ttkbootstrap import *#以內建tkinter
#先安裝Pillow模組(pip install pillow)，然後再匯入Image和ImageTk模組
import sys
import os
from tkinter import filedialog
from PIL import Image, ImageTk
"""
*表示匯入模組中的所有函數和物件(這樣就可以直接使用tkinter中的函數和物件，
而不需要每次都寫tkinter.指令)
"""


#######################定義函數########################
def open_file():
    global file_path#宣告file_path為全域變數，這樣在其他函數中也可以使用它
    #選擇檔案，initialdir是初始目錄，這裡設定為程式所在目錄
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])#filetypes是檔案類型，這裡設定為圖片檔案和所有檔案
    label2.config(text=file_path)#將選擇的檔案路徑顯示在label2上，config是用來修改元件屬性的函數，這裡修改了text屬性
def show_image():
    global file_path#宣告file_path為全域變數，這樣在其他函數中也可以使用它
    image = Image.open(file_path)#使用Pillow模組的Image.open()函數
    #調整圖片大小，讓他適合畫布大小
    #Image.LANCZOS是Pillow模組中的一種高品質的縮放濾鏡，可以在縮小圖片時保持較好的圖像質量
    #它會很仔細的把顏色混和好，讓圖片縮放打小後還是清楚好看，不會變得模糊或鋸齒狀
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)
    #轉換成Tkinter可以顯示的圖片格式
    photo = ImageTk.PhotoImage(image)
    #在畫布顯示圖片，圖片的左上角對齊畫布的左上角
    canvas.create_image(0, 0, anchor="nw", image=photo)
    #為了讓圖片不被垃圾回收機制回收，需要將tk_image保存在一個全域變數中，這樣它就不會被回收了
    canvas.image = photo
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
label = Label(window, text="選擇檔案:")#建立一個標籤，text是標籤上的文字
label.grid(row=0, column=0, sticky="E")#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式)

label2 = Label(window, text="無")#建立一個標籤，text是標籤上的文字
label2.grid(row=0, column=1, sticky="E")#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式)
#######################建立按鈕########################
button = Button(window, text="瀏覽",command = open_file, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button.grid(row=0, column=2, sticky="W")#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式)

button2 = Button(window, text="顯示",command =show_image, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button2.grid(row=1, column=0, columnspan=3,sticky="EW")#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式)

canvas = Canvas(window, width=400, height=400)#建立一個畫布，width是寬度，height是高度
canvas.grid(row=2, column=0, columnspan=2)#將畫布加入主視窗，並設定畫布的位置和間距(row是橫排，column是直排)
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