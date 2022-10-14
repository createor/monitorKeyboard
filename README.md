# 监控window键盘键入关键字

版本说明

```
python:3.6.5
```

下载相关第三方库

```
pip install pynput==1.7.6
pip install pyinstaller==4.10
```

打包成exe可执行文件

```bash
pyinstaller -F -w -i keyboard.ico monitor.py
```

添加到开机自启动

```
执行autoStart.bat批处理文件即可
```

相关配置说明

```
appName = "SecureCRT"  # 程序标题，例如Xshell程序标题含有Xshell字样，根据需求更改
rules = ["su -", "su", "sudo"]  # 过滤规则，根据需要添加即可
```

