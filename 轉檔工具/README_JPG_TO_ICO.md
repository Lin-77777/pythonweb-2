# JPG to ICO 轉換工具

## 概述
這是一個Python工具程式，用於將JPG、PNG、BMP等圖片格式轉換為ICO格式。

## 功能特性
- ✅ 支援多種輸入格式（JPG、JPEG、PNG、BMP、GIF）
- ✅ 提供圖形用戶界面（GUI）
- ✅ 支援命令行模式
- ✅ 自訂ICO尺寸（16、32、64、128、256像素）
- ✅ 自動背景處理（白色背景）
- ✅ 錯誤驗證和處理

## 系統需求
- Python 3.6+
- Pillow（PIL）庫
- tkinter（通常隨Python安裝）

## 安裝依賴
```bash
pip install Pillow
```

## 使用方法

### 方法1：圖形用戶界面（推薦）
```bash
python jpg_to_ico_tool.py
```

然後按照以下步驟：
1. 點擊「瀏覽」按鈕選擇輸入圖片
2. （可選）點擊「瀏覽」選擇輸出位置，或自動產生
3. 選擇所需的ICO尺寸
4. 點擊「開始轉換」

### 方法2：命令行模式
```bash
# 基本用法（使用預設256x256尺寸）
python jpg_to_ico_tool.py input.jpg output.ico

# 指定自訂尺寸
python jpg_to_ico_tool.py input.jpg output.ico 128x128

# 支援的尺寸：16x16, 32x32, 64x64, 128x128, 256x256
```

## 使用範例

### 範例1：轉換單個檔案
```bash
python jpg_to_ico_tool.py my_image.jpg my_icon.ico
```

### 範例2：使用128x128尺寸
```bash
python jpg_to_ico_tool.py photo.jpg favicon.ico 128x128
```

### 範例3：GUI界面
```bash
python jpg_to_ico_tool.py
# 然後操作界面進行轉換
```

## 支援的格式
### 輸入格式
- JPG / JPEG
- PNG
- BMP
- GIF

### 輸出格式
- ICO（Windows Icon Format）

## 注意事項
1. 輸入圖片會自動縮放到指定尺寸
2. 非正方形圖片會在白色背景上居中
3. 輸出檔案副檔名必須是 `.ico`
4. 轉換後的ICO檔案可用於Windows應用程式、網站favicon等

## 程式碼結構
- `JPGtoICOConverter` 類別：核心轉換邏輯
- `JPGtoICOGUI` 類別：圖形用戶界面
- `main()` 函數：入口點（支援CLI和GUI模式自動判斷）

## 許可證
MIT License

## 作者
Python JPG to ICO Tool v1.0
