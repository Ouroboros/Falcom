@ECHO OFF
FOR %%i IN (..\DecodeData\EV*.txt) DO IF EXIST MES_%%~nxi Copy %%i .