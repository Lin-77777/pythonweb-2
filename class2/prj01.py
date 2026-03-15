#######################匯入模組#######################
#匯入tkinter模組
from tkinter import *
"""
*表示匯入模組中的所有函數和物件(這樣就可以直接使用tkinter中的函數和物件，
而不需要每次都寫tkinter.指令)
"""

#######################定義函數########################
def x():
    if label1.cget("text") == "green":
        """
        cget()是tkinter模組中的一個方法，用於獲取元件的屬性值。當你調用cget()時，你可以傳遞屬性名稱來獲取該屬性的值。
        在這裡，我們使用cget("text")來獲取label1的text屬性值，並檢查它是否等於"green"。
        """
        
        label1.config(text="blue",fg="black",bg="blue")
            
    else:
        label1.config(text="green",fg="black",bg="green")
"""
變數版本

def x():
    #透過change變數來記錄狀態，當按鈕被點擊時，如果change是False，就將標籤的文字設置為"blue"，背景顏色設置為藍色；如果change是True，就將標籤的文字設置為"green"，背景顏色設置為綠色。最後，將change的值取反，這樣下次按鈕被點擊時就會切換到另一種狀態。
    global change
    if change ==False:
        label1.config(text="blue",fg="black",bg="blue")
    else:
        label1.config(text="green",fg="black",bg="green")
    change = not (change)
#初始值設為false，這樣第一次按鈕被點擊時就會切換到藍色狀態。
change = False
"""
#######################建立視窗########################
#建立主視窗
window = Tk()#Tk()是tkinter模組中的一個物件，用於創建主視窗對象。當你調用Tk()時，它會創建一個新的主視窗。
window.title("我的第一個GUI應用程式")#設定視窗標題
###################建立按鈕########################
#建立按鈕1，並設定點擊事件為button1_click函數
btn1 = Button(window, text="切換顏色", command=x)
#將按鈕加入主視窗
btn1.pack()
"""
pack()是tkinter模組中的一個方法，用於將元件（如按鈕）添加到視窗中。
當你調用pack()時，它會自動將元件放置在視窗的適當位置，並根據需要調整大小和位置。
"""

######################建立標籤########################
#建立標籤1，顯示一些文字
label1 = Label(window, text="green",fg="black",bg="green")#text是標籤顯示的文字，現在先空著，方便後續放文字
#將標籤加入主視窗
label1.pack()
#######################運行應用程式########################
#運行主事件循環，等待用戶操作

  
window.mainloop()
"""
    mainloop()是tkinter模組中的一個方法，用於啟動主事件循環。當你調用mainloop()時，
    它會進入一個無限循環，等待用戶的操作（如按鈕點擊、鍵盤輸入等）。在這個循環中，tkinter會處理所有的事件，
    並根據用戶的操作更新界面。只有當你關閉主視窗時，mainloop()才會結束，程序才會退出。
"""




#課堂小筆記
"""
物件才會###.####()
物件跟類別是同一個意思
指令()會直接執行，而指令不加()則是將函數本身作為一個物件傳遞，這樣就可以在需要的時候找它。
在planmode中可以用請提出計畫讓ai這樣就可以檢查計畫是符合你的需求
c.get是config.get的簡寫，這樣就可以直接使用c.get()來獲取元件c的屬性值，例:c.get("text")可以獲取元件c的text屬性值。
### = not (###)是將變數###的值取反，如果###是True，則變為False；如果###是False，則變為True。
"""