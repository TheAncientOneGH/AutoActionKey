@echo off

TITLE=AutoActionKey
cd %~dp0
set /a savereq=0
set "applock=%~dp0aak.lock"
set "venvname=.aak"
set "verstr=1.3"
cls
if exist "%applock%" (
    echo %TITLE% already running!
    echo.
    echo If this is a mistake, you may not have
    echo shutdown a session properly. Please
    echo delete '%applock%' to fix.
    echo.
    pause
    exit /b
)
echo Please wait...
echo.
if NOT exist "%~dp0embedded\Scripts\pip.exe" (
	%~dp0embedded\python.exe "%~dp0embedded\get-pip.py" --no-warn-script-location
)
"%~dp0embedded\python.exe" -m pip cache purge
cls
echo Please wait...
if NOT exist "%~dp0%venvname%\" (
	%~dp0embedded\python.exe -m pip install virtualenv --no-warn-script-location
	%~dp0embedded\python.exe -m virtualenv %venvname%
	call %venvname%\Scripts\activate
) else (
	rem Error prevention, just in case
	call %venvname%\Scripts\deactivate
	call %venvname%\Scripts\activate
)
cls
echo Please wait...
"%~dp0embedded\python.exe" -m pip install --upgrade pip
echo running > "%applock%"
cls
"%~dp0embedded\python.exe" "%~dp0autoactionkey.py"
echo.
if %savereq% == 1 (
	"%~dp0embedded\python.exe" -m pip freeze > "%~dp0requirements.txt"
)
del "%applock%"
call %venvname%\Scripts\deactivate
exit /b
