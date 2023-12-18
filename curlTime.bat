@echo off
setlocal enabledelayedexpansion

rem 定义测试端口列表
set ports=80 443 8443

rem 定义测试次数
set num_iterations=10

set dir=E:\Current\00_Project\COMNET\COMNET_PJ\curl

rem 定义输出文件
set output_file=%dir%\time_result2.txt

rem 遍历端口
for %%p in (%ports%) do (
    set port=%%p
    set result_file=%dir%\!port!_time2.txt
    echo Testing port !port! >> !output_file!

    rem 进行多次测试并统计平均值
    set total_connect_time=0
    set total_starttransfer_time=0
    set total_total_time=0

    for /l %%i in (1,1,%num_iterations%) do (
        curl -o nul -s -w "Connect time: %%{time_connect} s\nStart transfer time: %%{time_starttransfer} s\nTotal time: %%{time_total} s\n" 111.229.132.28:!port! >> !result_file!

        rem 提取时间数据并累加
        rem for /f "tokens=2 delims=:" %%a in ('type !result_file! ^| find "Connect time"') do set total_connect_time+=%%a
        rem for /f "tokens=2 delims=:" %%b in ('type !result_file! ^| find "Start transfer time"') do set total_starttransfer_time+=%%b
        rem for /f "tokens=2 delims=:" %%c in ('type !result_file! ^| find "Total time"') do set total_total_time+=%%c
        set /p connect_time=< !result_file! | find "Connect time"
        set /p starttransfer_time=< !result_file! | find "Start transfer time"
        set /p total_time=< !result_file! | find "Total time"

        rem 提取时间数据并累加
        set /a total_connect_time+=!connect_time:~14,-2!
        set /a total_starttransfer_time+=!starttransfer_time:~20,-2!
        set /a total_total_time+=!total_time:~13,-2!
    )
    rem 计算平均值
    set /a avg_connect_time=total_connect_time / %num_iterations%
    set /a avg_starttransfer_time=total_starttransfer_time / %num_iterations%
    set /a avg_total_time=total_total_time / %num_iterations%

    echo Average Connect time: !avg_connect_time! s >> !output_file!
    echo Average Start transfer time: !avg_starttransfer_time! s >> !output_file!
    echo Average Total time: !avg_total_time! s >> !output_file!

    echo. >> !output_file!
)

echo "Done, output to %output_file%"
