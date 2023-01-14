#!/bin/bash

cd `dirname $0` # カレントディレクトリに移動

call .\env\Scripts\activate.bat

py .\src\main.py

pause