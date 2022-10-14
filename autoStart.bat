@echo off

set AppName=monitor.exe
set FilePath=%~dp0
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Monitor /t reg_sz /d "%FilePath%%monitor.exe"