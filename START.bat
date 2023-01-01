powershell .\set_env.ps1

py -m pip install --upgrade pip

call .\env\Scripts\activate.bat

py .\src\main.py

pause