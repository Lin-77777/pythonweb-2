#######################匯入模組#######################
#匯入tkinter模組
from tkinter import *
#先安裝Pillow模組(pip install pillow)，然後再匯入Image和ImageTk模組
from PIL import Image, ImageTk
import sys
import os
"""
*表示匯入模組中的所有函數和物件(這樣就可以直接使用tkinter中的函數和物件，
而不需要每次都寫tkinter.指令)
"""
#######################設定工作目錄########################
os.chdir(sys.path[0])#chdir是change directory的縮寫，os.chdir()用於把vscode目前位置改變成()裡的。
"""
將工作目錄切換到當前程式所在的資料夾，這樣就可以讀取同一個資料夾中的其他檔案，
例如圖片檔案，這樣就不需要寫絕對路徑了。
"""
#######################定義函數########################
def move_circle(event):#定義一個函數，用於移動圓形(event是事件物件，包含了按鍵事件的相關信息)
    
    if event.keysym == "Up":#如果按下的是上鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(circle, 0, -10)#將圓形向上移動10個像素，x方向不變，y方向減少10
    elif event.keysym == "Down":#如果按下的是下鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(circle, 0, 10)#將圓形向下移動10個像素，x方向不變，y方向增加10
    elif event.keysym == "Left":#如果按下的是左鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(circle, -10, 0)#將圓形向左移動10個像素，x方向減少10，y方向不變
    elif event.keysym == "Right":#如果按下的是右鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(circle, 10, 0)#將圓形向右移動10個像素，x方向增加10，y方向不變
    elif event.keysym == "w":#如果按下的是w鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(rect, 0, -10)#將圓形向上移動10個像素，x方向不變，y方向減少10
    elif event.keysym == "s":#如果按下的是s鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(rect, 0, 10)#將圓形向下移動10個像素，x方向不變，y方向增加10
    elif event.keysym == "a":#如果按下的是a鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(rect, -10, 0)#將圓形向左移動10個像素，x方向減少10，y方向不變
    elif event.keysym == "d":#如果按下的是d鍵(用event.keysym可以獲取按鍵的名稱)
        canvas.move(rect, 10, 0)#將圓形向右移動10個像素，x方向增加10，y方向不變
def exit_fun():
    window.destroy()#退出視窗
#######################建立視窗########################
#建立主視窗
window = Tk()#Tk()是tkinter模組中的一個物件，用於創建主視窗對象。當你調用Tk()時，它會創建一個新的主視窗。
window.title("我的第一個GUI應用程式")#設定視窗標題
#######################建立畫布########################
canvas = Canvas(window, width=400, height=300, bg="white")#建立一個畫布，指定寬度、高度和背景顏色
canvas.pack()#將畫布加入主視窗

#######################設定視窗圖片########################
window.iconbitmap("gay.ico")#設定視窗圖示，icon.ico是同一個資料夾中的圖示檔案(一定要是.ico格式的圖示檔案)，這樣就不需要寫絕對路徑了。

#######################載入圖片########################
#使用PIL模組的Image載入圖片

image = Image.open("gay.jpg")#使用PIL模組的Image類別載入圖片
#注意:需保留img的參照，否則圖片會被python的垃圾回收機制回收掉，導致圖片無法顯示。
img = ImageTk.PhotoImage(image)#將PIL的Image物件轉換為tkinter可以使用的PhotoImage物件，這樣就可以在畫布上顯示圖片了。
#######################顯示圖片########################
#在畫布上顯示圖片，(200,150)是圖片的中心位置，image是要顯示的圖片物件
my_img = canvas.create_image(200, 150, image=img)#=變數為必要，只是為了方便後續修改位置等要素
#######################畫圖形########################
#在畫布上畫一個紅色的圓形，(50,50)是圓形的左上角坐標，(150,150)是圓形的右下角坐標
circle = canvas.create_oval(50, 50, 150, 150, fill="red")
#在畫布上畫一個藍色的矩形，(250,50)是矩形的左上角坐標，(350,150)是矩形的右下角坐標
rect = canvas.create_rectangle(250, 50, 350, 150, fill="blue")
#在畫布上顯示文字，(200,250)是文字的坐標，text是要顯示的文字內容，font是文字的字體和大小，fill是文字的顏色
msg = canvas.create_text(200, 250, text="I'm a gay", font=("Arial", 20), fill="green")
#######################綁定按鍵事件########################
canvas.bind_all("<Key>", move_circle)#綁定按鍵事件，當按下任意鍵時，會觸發move_circle函數
###################建立按鈕########################
quit_button = Button(window, text="Quit", command=exit_fun)#建立一個按鈕，text是按鈕上的文字，command是按鈕被點擊時要執行的函數，這裡是window.quit()，用於關閉視窗
quit_button.pack()#將按鈕加入主視窗，並設定按鈕與其他元素的間距(pady是垂直間距)
######################建立標籤########################

#######################運行應用程式########################
#運行主事件循環，等待用戶操作

  
window.mainloop()
"""
    mainloop()是tkinter模組中的一個方法，用於啟動主事件循環。當你調用mainloop()時，
    它會進入一個無限循環，等待用戶的操作（如按鈕點擊、鍵盤輸入等）。在這個循環中，tkinter會處理所有的事件，
    並根據用戶的操作更新界面。只有當你關閉主視窗時，mainloop()才會結束，程序才會退出。
"""




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

'''