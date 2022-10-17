# -*- encoding:utf-8 -*-
'''
@File     :     monitor.py
@Time     :     2022/10/17
@Author   :     createor
@Version  :     1.0.0
@Contact  :     751835040@qq.com
'''
from pynput import keyboard
from pynput import mouse
import win32gui

item = []
currentApp = ""
appName = "SecureCRT"
# appName = "Xshell"


def on_press(key):  # 键盘按下事件，输入
    global item
    global currentApp
    global appName
    if appName in currentApp:  # 指定监听的程序
        if key == keyboard.Key.enter:  # 回车事件enter
            # print("触发回车")
            item = []
        elif key == keyboard.Key.backspace:  # 删除键backspace
            # print("触发删除")
            if len(item) != 0:
                item = item[:len(item) - 1]
        elif key == keyboard.Key.space:  # 空格space
            # print("触发空格")
            item.append(" ")
        elif str(key) == r"'\x03'":  # 组合键ctrl + c
            # print("触发ctrl + c")
            item = []
        else:
            try:
                item.append(key.char)
            except AttributeError:
                # print(key)
                pass
        return False


def get_vk(key):  # 获取键盘码
    if isinstance(key, keyboard.Key):
        return key.value.vk
    elif isinstance(key, keyboard._win32.KeyCode):
        return key.vk
    else:
        return None


def check(word):  # 校验输入
    rules = ["su -", "su", "sudo"]  # 过滤规则
    for rule in rules:
        # if str(word).strip() in rule:
        if str(word).strip() == str(rule).strip():
            return False
    # if str(word).strip() in rules:
    #     return False
    return True


def foucs(x, y, button, pressed):  # 鼠标点击事件
    global currentApp
    if pressed and button == mouse.Button.left:  # 鼠标左键点击聚焦程序输入
        currentApp = getApp()


def on_move(x, y):  # 鼠标移动事件
    global currentApp
    currentApp = getApp()


def getApp():  # 获取当前键入程序标题名
    current_windows = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(current_windows)
    return title


def main():  # 主程序
    while True:
        # 监听鼠标事件
        mouseListener = mouse.Listener(on_move=on_move, on_click=foucs)
        mouseListener.start()
        # 监听键盘事件

        def win32_event_filter(msg, data):
            global item
            global currentApp
            global appName
            if appName in currentApp:  # 指定监听的程序
                if data.vkCode == get_vk(keyboard.Key.enter):  # 回车键
                    word = "".join(item)  # 拼接输入字符
                    if not check(word):  # 校验不通过
                        keyboardListener.suppress_event()  # 抑制键盘回车事件

        with keyboard.Listener(on_press=on_press, win32_event_filter=win32_event_filter) as keyboardListener:
            keyboardListener.join()


if __name__ == "__main__":
    main()
