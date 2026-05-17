####################### 模組 #######################
# [asyncio]
# Python 內建的異步編程模組。概念像「任務小管家」：遇到需要等待網路回應的事件時，
# 會先去安排處理別的事，避免整個程式卡住。(與多執行緒不同，它是利用單執行緒不斷切換任務)
import asyncio

# [discord]
# Discord Bot 開發核心套件 (終端機安裝：pip install -U discord.py)
import discord

# [os & dotenv]
# os 用來讀取系統環境變數；load_dotenv 用來讀取 .env 檔案中的環境變數
import os
from dotenv import load_dotenv

####################### 初始化 #######################
# 讀取 .env 檔，讓程式可以拿到隱藏的敏感資訊 (如 DC_BOT_TOKEN)
load_dotenv()

# 【事件循環 Event Loop】可以想成「非同步任務轉盤」，負責安排工作的先後順序。
# Python 3.10+ 在主程式裡不一定會自動準備好，因此手動建立一個給 Discord 模組使用。
asyncio.set_event_loop(asyncio.new_event_loop())

# 【Intents】設定機器人需要監聽哪些事件的權限
intent = discord.Intents.default()
# 啟用讀取訊息內容的權限 (必要設定：這樣機器人才能根據訊息內容做出反應)
intent.message_content = True

# 【Client】與 Discord API 交互的主要接口 (處理接收事件、發送訊息等操作)
bot = discord.Client(intents=intent)

# 【CommandTree】用來管理機器人的應用程式指令 (Slash Commands / 斜線指令)
tree = discord.app_commands.CommandTree(bot)


####################### 事件 #######################
# 【觀念補充】
# @bot.event 叫做「裝飾器 (Decorator)」，可以想像成幫下方的函式貼上「事件處理員」的標籤。
# def : 一般函式，通常會照順序一路執行完畢。
# async def : 異步函式，可搭配 await 使用。遇到需要等待的工作時，可以暫停讓出控制權，完成後再回來繼續。


@bot.event
async def on_ready():
    # 當機器人成功連線至 Discord 並準備就緒時，會觸發此函式
    print(f"We have logged in as {bot.user}")

    # 將程式內的指令清單同步至 Discord 伺服器 (確保修改後的指令能生效)
    await tree.sync()


"""
【關於 async 與 await】
兩者是成對使用的：
- async def：用來定義異步函式，執行中可暫停，不阻塞整個程式。
- await：用來等待異步操作完成。遇到 await 時程式會暫停在該行，直到操作完成才繼續。
(概念類似 Arduino 中用 millis() 替代 delay()，避免卡死整個程式)
"""


@bot.event
async def on_message(
    message,
):
    # 當頻道有新訊息產生時會觸發此函式 (message 就是該則訊息的資料包)

    # 檢查訊息的作者是否為機器人自己。如果是，就直接結束函式，避免無限迴圈。
    if message.author == bot.user:
        return

    # 檢查訊息內容是否以 "hi" 開頭
    if message.content == "hi":
        # 回傳訊息需要透過網路回送給 Discord，因此要用 await 等待發送完成
        await message.channel.send("Hello!")


####################### 指令 #######################
# 【@tree.command】指令註冊裝飾器
# name: 指令名稱 (需與下方函式名稱一致，用戶輸入 /hello 即可觸發)
# description: 指令的描述與說明
@tree.command(name="hello", description="A simple ping command")
async def hello(interaction: discord.Interaction):
    """輸入 /hello 就會觸發這個函式"""

    # 參數後面的 : discord.Interaction 是定義資料型態。
    # interaction 是本次使用指令時傳來的資料包 (包含使用者資訊、頻道資訊、指令參數等)

    # 回覆使用者的指令 (需透過網路，使用 await 等待)
    await interaction.response.send_message("Hello!")


####################### 啟動 #######################


def main():
    # 啟動機器人，使用從環境變數 (DC_BOT_TOKEN) 獲取的 Token 來連線
    bot.run(os.getenv("DC_BOT_TOKEN"))


# __name__ 是 Python 內建變數。
# 當腳本被「直接執行」時，__name__ 的值會是 "__main__"。
# 若這支檔案是被當作模組「匯入 (import)」到其他檔案，則不會執行底下區塊，避免產生不必要的副作用。


if __name__ == "__main__":
    main()


####################### 課堂小筆記 #######################
"""
【必要套件安裝指令】
pip install -U discord.py       (Discord Bot 開發的必要套件)
pip install -U python-dotenv    (讀取 .env 檔案資料用的套件)

【.gitignore 觀念】
- 用途：讓 Git 忽略特定的檔案，不將這些檔案提交到版本控制系統 (如 GitHub) 中。
- 用法：在 VSCode 找到 .env 檔案按右鍵選擇 "Add to .gitignore"，或手動在 .gitignore 檔案中寫入 ".env"。
- 目的：避免將敏感資訊 (Token) 或不必要的檔案上傳，保持專案整潔與安全。

【其他補充】
- @bot.event 原理類似筆記圖片，但它是包裝上 Discord 的官方模板 (讓它可以運行的必要程式)。
- `*` 符號在程式碼中通常代表「所有的 / 全部」的意思。
"""
