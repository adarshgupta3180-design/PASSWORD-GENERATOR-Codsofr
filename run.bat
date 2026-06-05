@echo off
title ShieldPass - Password Generator
echo Starting ShieldPass...
set "TCL_LIBRARY=C:\Users\Aman\AppData\Local\Programs\Python\Python314\tcl\tcl8.6"
set "TK_LIBRARY=C:\Users\Aman\AppData\Local\Programs\Python\Python314\tcl\tk8.6"
C:\Python314\python.exe main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: App failed to start. Ensure Python 3 is installed.
    pause
)
