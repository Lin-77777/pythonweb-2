# 認識裝飾詞的用法(Decorator)的用法
# ================================================
# 第一階段:把函式當作參數傳遞給另一個函式
# ================================================


# 定義一個簡單的函式
def hello():
    print("Hello, World!")


# 定義一個可以[接收函式]當作參數的函式
def run_with_announce(func):
    print("即將執行函式...")
    func()  # 執行傳入的函式
    print("函式執行完畢!")


print("直接呼叫hello函式:")
hello()  # 直接呼叫hello函式

print()

print("使用run_with_announce來呼叫hello函式:")
run_with_announce(
    hello
)  # 把say_hello函式當作參數傳入run_with_announce函式，這樣就會在執行hello函式前後印出一些訊息


# ===============================================
# 第二階段:使用裝飾詞來包裝函式
# ===============================================
# 核心概念:用一個函式把另一個函式[包裝起來]
# 就像在禮物外面包一層包裝紙


def gift_wrap(func):
    def wrapped_func():
        print("這是包裝紙，裡面有一個禮物...")
        func()  # 執行傳入的函式
        print("禮物已經被打開了!")

    return wrapped_func  # 回傳包裝好的函式


def hello():
    print("這是禮物: Hello, World!")


# 手動包裝:把hello函式包裝起來，並覆蓋原本的hello函式
hello = gift_wrap(hello)
print("呼叫包裝後的hello函式:")
# 現在已經是包裝後的hello函式了。
hello()  # 呼叫包裝後的hello函式，這樣就會先印出包裝紙的訊息，再執行hello函式，最後印出禮物已經被打開的訊息
print()  # 不重要，只是要做出一行空行用的


# ================================================
# 第三階段:使用@符號來簡化裝飾詞的使用
# ================================================

"""
@gift_wrap是上方定義過的那個gift_wrap函式(一定要先定義gift_wrap函式，否則無法使用)，
所以這裡的意思和hello = gift_wrap(hello)是一樣的，只是使用了@符號來簡化裝飾詞的使用，這樣就不需要手動包裝了。
"""


@gift_wrap  # 使用@符號來裝飾hello函式，這樣就不需要手動包裝了
def hello():
    print("這是禮物: Hello, World!")


hello()  # 呼叫裝飾過的hello函式，這樣就會先印出包裝紙的訊息，再執行hello函式，最後印出禮物已經被打開的訊息

print()  # 不重要，只是要做出一行空行用的
# ================================================
# 第四階段:帶參數的裝飾詞
# ================================================


# 外層函式:接收裝飾詞的參數(name、decoration)
# 中層函式:接收被裝飾的函式(func)
# 內層函式:包裝後實際執行的函式(wrapped_func)
def personalized_gift_wrap(name, decoration):  # 外層:接收參數
    print(f"[登記] 指令/{name}:{decoration}")

    def decorator(func):  # 中層:接收函式
        def wrapped_func():  # 內層:包裝後的函式
            print(f"[執行] 指令/{name}")
            func()  # 執行傳入的函式

        return wrapped_func

    return decorator  # 回傳中層(真正的裝飾器)


# @personalized_gift_wrap(name="hello", decoration="包裝紙")
# 等同於:
# step1 = personalized_gift_wrap(name="hello", decoration="包裝紙")  #得到 decorator
# step2 = step1(hello)      #得到 wrapper
@personalized_gift_wrap(
    name="hello", decoration="包裝紙"
)  # 就算是沒有使用hello()也會執行print(f"[登記] 指令/{name}:{decoration}")，因為@也是一種函式呼叫
def hello():
    print("這是禮物: Hello, World!")


hello()  # 執行包裝後的版本
