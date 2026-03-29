"""
JPG to ICO Converter Tool
功能: 將JPG圖片轉換為ICO格式的工具程式
"""

import os
import sys
from pathlib import Path
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


class JPGtoICOConverter:
    """JPG到ICO的轉換器類別"""
    
    def __init__(self):
        self.supported_input_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        self.ico_size_options = [(16, 16), (32, 32), (64, 64), (128, 128), (256, 256)]
    
    def convert(self, input_path, output_path=None, size=(256, 256)):
        """
        轉換JPG圖片為ICO格式
        
        參數:
            input_path (str): 輸入圖片路徑
            output_path (str): 輸出ICO檔案路徑（可選）
            size (tuple): ICO大小，預設(256, 256)
        
        返回:
            bool: 轉換成功返回True，失敗返回False
            str: 結果訊息
        """
        try:
            # 驗證輸入檔案
            input_file = Path(input_path)
            if not input_file.exists():
                return False, f"錯誤: 輸入檔案不存在: {input_path}"
            
            if input_file.suffix.lower() not in self.supported_input_formats:
                return False, f"錯誤: 不支援的格式。支援格式: {', '.join(self.supported_input_formats)}"
            
            # 設定輸出路徑
            if output_path is None:
                output_path = input_file.stem + '.ico'
            
            output_file = Path(output_path)
            
            # 開啟並轉換圖片
            with Image.open(input_file) as img:
                # 如果圖片有透明度通道以外的RGBA，轉換為RGB
                if img.mode in ('RGBA', 'LA', 'P'):
                    # 建立白色背景
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # 調整大小
                img.thumbnail(size, Image.Resampling.LANCZOS)
                
                # 建立正方形畫布（如果不是正方形）
                if img.size[0] != img.size[1]:
                    side = max(img.size)
                    square = Image.new('RGB', (side, side), (255, 255, 255))
                    offset = ((side - img.size[0]) // 2, (side - img.size[1]) // 2)
                    square.paste(img, offset)
                    img = square
                
                # 保存為ICO
                img.save(str(output_file), 'ICO')
            
            return True, f"成功! 已轉換為: {output_path}"
        
        except Exception as e:
            return False, f"轉換失敗: {str(e)}"


class JPGtoICOGUI:
    """圖形用戶界面"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("JPG to ICO 轉換工具")
        self.root.geometry("500x300")
        self.converter = JPGtoICOConverter()
        self.input_file = None
        self.output_file = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """設置用戶界面"""
        # 標題
        title_label = ttk.Label(self.root, text="JPG to ICO 轉換工具", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 輸入檔案框架
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        ttk.Label(input_frame, text="輸入檔案:").pack(side="left")
        self.input_label = ttk.Label(input_frame, text="未選擇", foreground="gray")
        self.input_label.pack(side="left", padx=10)
        ttk.Button(input_frame, text="瀏覽", command=self.select_input_file).pack(side="right")
        
        # 輸出檔案框架
        output_frame = ttk.Frame(self.root)
        output_frame.pack(pady=10, padx=20, fill="x")
        
        ttk.Label(output_frame, text="輸出檔案:").pack(side="left")
        self.output_label = ttk.Label(output_frame, text="自動產生", foreground="gray")
        self.output_label.pack(side="left", padx=10)
        ttk.Button(output_frame, text="瀏覽", command=self.select_output_file).pack(side="right")
        
        # ICO尺寸框架
        size_frame = ttk.Frame(self.root)
        size_frame.pack(pady=10, padx=20, fill="x")
        
        ttk.Label(size_frame, text="ICO尺寸:").pack(side="left")
        self.size_var = tk.StringVar(value="256x256")
        self.size_combo = ttk.Combobox(size_frame, textvariable=self.size_var, 
                                      values=["16x16", "32x32", "64x64", "128x128", "256x256"],
                                      state="readonly", width=10)
        self.size_combo.pack(side="left", padx=10)
        
        # 轉換按鈕
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="開始轉換", command=self.convert_file).pack(side="left", padx=5)
        ttk.Button(button_frame, text="重設", command=self.reset_form).pack(side="left", padx=5)
        
        # 狀態標籤
        self.status_label = ttk.Label(self.root, text="", foreground="blue")
        self.status_label.pack(pady=10)
    
    def select_input_file(self):
        """選擇輸入檔案"""
        file_types = [("圖片檔案", "*.jpg *.jpeg *.png *.bmp *.gif"), ("所有檔案", "*.*")]
        file = filedialog.askopenfilename(title="選擇輸入圖片", filetypes=file_types)
        if file:
            self.input_file = file
            self.input_label.config(text=Path(file).name, foreground="black")
    
    def select_output_file(self):
        """選擇輸出檔案"""
        file = filedialog.asksaveasfilename(title="選擇輸出位置", 
                                           defaultextension=".ico",
                                           filetypes=[("ICO檔案", "*.ico"), ("所有檔案", "*.*")])
        if file:
            self.output_file = file
            self.output_label.config(text=Path(file).name, foreground="black")
    
    def convert_file(self):
        """轉換檔案"""
        if not self.input_file:
            messagebox.showwarning("警告", "請先選擇輸入檔案")
            return
        
        # 解析尺寸
        size_str = self.size_var.get()
        size = tuple(map(int, size_str.split('x')))
        
        # 執行轉換
        success, message = self.converter.convert(self.input_file, self.output_file, size)
        
        if success:
            messagebox.showinfo("成功", message)
            self.status_label.config(text=message, foreground="green")
            self.reset_form()
        else:
            messagebox.showerror("錯誤", message)
            self.status_label.config(text=message, foreground="red")
    
    def reset_form(self):
        """重設表單"""
        self.input_file = None
        self.output_file = None
        self.input_label.config(text="未選擇", foreground="gray")
        self.output_label.config(text="自動產生", foreground="gray")
        self.status_label.config(text="", foreground="blue")


def main():
    """主程式入口"""
    if len(sys.argv) > 1:
        # 命令行模式
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        size_str = sys.argv[3] if len(sys.argv) > 3 else "256x256"
        
        try:
            size = tuple(map(int, size_str.split('x')))
        except:
            size = (256, 256)
        
        converter = JPGtoICOConverter()
        success, message = converter.convert(input_path, output_path, size)
        print(message)
        sys.exit(0 if success else 1)
    else:
        # GUI模式
        root = tk.Tk()
        app = JPGtoICOGUI(root)
        root.mainloop()


if __name__ == "__main__":
    main()
