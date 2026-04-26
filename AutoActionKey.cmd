@echo off
TITLE=AutoActionKey
cls

if NOT exist "%~dp0embedded\Scripts\pip.exe" (
	%~dp0\embedded\python.exe "%~dp0embedded\get-pip.py" "--no-warn-script-location"
)

%~dp0\embedded\python.exe "%~dp0autoactionkey.py" "--no-warn-script-location"

pause
rem exit
