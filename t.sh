@echo off
chcp 65001
echo Enabling developer mode on Windows...
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1" 2>&1 >nul
echo Windows Developer mode done!
echo Restarting USB connection to fix random connection on/off bug...
net stop "usbaap" 2>&1 >nul
net start "usbaap" 2>&1 >nul
echo USB connection restarted. Done.
exit /b 0
