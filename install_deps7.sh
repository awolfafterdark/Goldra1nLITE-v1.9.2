@echo off
REM dependencies check
echo Checking for required dependencies...

where git >nul 2>nul || (
    echo Error: Git is not installed. Please install Git and try again.
    exit /b 1
)

where choco >nul 2>nul || (
    echo Error: Chocolatey is not installed. Please install Chocolatey and try again.
    exit /b 1
)

echo Dependencies are met. Proceeding with installation...

echo This may take some time to install. Just wait...
echo If you have a slow computer, I do not recommend it!!!
echo Going to install palera1n GUI dependencies in 3 seconds...
echo.
ping 127.0.0.1 -n 3 >nul

echo You may need to enter your password...
REM No need to run sudo on Windows, as we are running as administrator.

echo Uninstalling Homebrew...
powershell.exe -Command "Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh' -OutFile uninstall-homebrew.sh"
.\uninstall-homebrew.sh

echo Installing Chocolatey...
powershell.exe -ExecutionPolicy Bypass -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"

echo Installing Git...
choco install git -y

echo Installing Homebrew...
powershell.exe -Command "Invoke-WebRequest -UseBasicParsing 'https://raw.githubusercontent.com/Homebrew/install/master/install.sh' -OutFile install-homebrew.sh"
.\install-homebrew.sh

echo Setting up Homebrew for Windows...
setx HOMEBREW_PREFIX %USERPROFILE%\.homebrew
setx HOMEBREW_CELLAR %USERPROFILE%\.homebrew\Cellar
setx PATH %USERPROFILE%\.homebrew\bin;%USERPROFILE%\.homebrew\sbin;%PATH%

echo Installing dependencies...
brew install libusb
brew install libtool
brew install automake
brew install curl

echo Running part 2 of dependencies...
echo.
echo.
echo.
echo Installing dependencies 2...
echo.

echo Installing sshpass...
brew install esolitos/ipa/sshpass
echo Installing libmobiledevice...
brew install libimobiledevice
echo Installing brew python...
brew install python@3.10
echo.
echo Installing tk for GUI...
pip3 install tk
pip install tk
brew install python-tk@3.10
echo.
echo Installing pillow for GUI...
pip3 install Pillow
pip install Pillow

echo.
echo Finished installing dependencies!!!
echo.
echo Done!!!
echo.
exit /b 0
