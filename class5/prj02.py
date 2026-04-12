



#######################匯入模組#######################
from ttkbootstrap import *
import sys
import os
#####################設定工作目錄#####################
os.chdir(sys.path[0])#將工作目錄切換到程式所在的目錄，這樣就可以直接使用相對路徑來讀取檔案了
#######################定義函數########################
#顯示計算結果的函式
def show_result():
    
    entry_text = entry.get()#取得輸入框中的文字
    try:
        result = eval(entry_text)#eval是預設函數，可以將字串當成Python程式碼來執行，這裡用它來計算輸入的表達式
        
        label.config(text="計算結果: " + str(result))#將計算結果
    except:
        result = "輸入錯誤，請輸入合法的表達式"#如果計算過程中出現錯誤，則顯示錯誤訊息
        label.config(text=result)#將錯誤訊息顯示在標籤
#######################建立視窗########################
window = Tk()#建立視窗
window.title("我的第一個GUI應用程式")#設定視窗標題
########################建立標籤########################
#顯示計算結果的標籤
label = Label(window, text="計算結果")#建立一個標籤，text是標籤上的文字
label.grid(row=2, column=0,columnspan=2,padx=10, pady=10,sticky="W")#將標籤加入主視窗，並設定標籤的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
#############################建立按鈕########################

#顯示計算結果的按鈕
button = Button(window, text="顯示計算結果",command = show_result, style = "my.TButton")#建立一個按鈕，text是按鈕上的文字，style是按鈕的樣式，這裡使用了之前設定的"my.TButton"樣式
button.grid(row=2, column=2,columnspan=2, padx=10, pady=10,sticky="W")#將按鈕加入主視窗，並設定按鈕的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
######################建立輸入框########################
entry = Entry(window,width=30)#建立一個輸入框
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)#將輸入框加入主視窗，並設定輸入框的位置和間距(row是橫排，column是直排，sticky是對齊方式，padx是水平間距，pady是垂直間距)
#padx,pady是元件與元件之間的間距
########################設定字型########################
font_size = 20 #設定字型大小
window.option_add("*Font", ("Helvetica",font_size))#設定視窗的字型，*Font是tkinter中的一個選項，用於設定所有元件的字型
#設定預設字型為Helvetica，大小為font_size


#######################設定主題########################
style = Style(theme="cyborg")#設定主題，Style是ttkbootstrap模組中的一個類別，用於設定主題，theme是要使用的主題名稱
style.configure("my.TButton", font=("Helvetica", font_size))#設定"my.TButton"的字型和顏色，font是字型
#######################運行應用程式########################
window.mainloop()#運行主事件循環，這樣視窗就會保持開啟狀態，直到用戶關閉它。