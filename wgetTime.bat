@echo off
setlocal enabledelayedexpansion

set ports=80 443 8443
set dir=E:\Current\00_Project\COMNET\COMNET_PJ\wget
set iterations=10
for /l %%i in (1,1,%iterations%) do (
    echo Iteration: %%i

    for %%p in (%ports%) do (
        set port=%%p
        rem set output_file=!dir!\wget_!port!.txt
        set output_file=!dir!\wget_res.txt
        set "time_file=!dir!\!port!_time.txt"

        REM Record start time
        for /f "tokens=1-4 delims=:., " %%a in ('echo !TIME!') do (
            set /a "start_time=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
        )

        REM Your command here
        rem wget --no-check-certificate -S -v https://111.229.132.28:!port! -O !output_file! 2>&1
        wget --no-check-certificate -S https://111.229.132.28:!port! -O NUL

        REM Record end time
        for /f "tokens=1-4 delims=:., " %%a in ('echo !TIME!') do (
            set /a "end_time=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
        )

        rem for /f "tokens=1-4 delims=:., " %%a in ('wmic path win32_localtime get Hour^,Minute^,Second^,Millisecond /format:list ^| find "="') do (
        rem     set /a "start_time=((%%a*60)+1%%b %% 100)*60+1%%c %% 100*100+1%%d %% 100"
        rem )

        REM Calculate execution time
        set /a "execution_time=end_time - start_time"

        echo Execution time: !execution_time! milliseconds >> !time_file!
    )
)