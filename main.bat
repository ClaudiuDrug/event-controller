@ECHO OFF

SET CURRENTDIR=%CD%
SET VENVPATH=D:\PyVenvs\event-controller_venv3.7
SET SCRIPTPATH=%CURRENTDIR%

CALL %VENVPATH%\Scripts\activate

python -O %SCRIPTPATH%\main.py

CALL %VENVPATH%\Scripts\deactivate

EXIT %ERRORLEVEL%