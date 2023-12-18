@echo off
setlocal enabledelayedexpansion

rem 定义端口列表
set ports=80 443 8443

rem 读取 endpoints.json 文件内容
for %%p in (%ports%) do (
    set port=%%p
    set output_file=E:\Current\00_Project\COMNET\COMNET_PJ\curl\!port!_result.txt

    for /f "tokens=* delims=" %%a in (endpoints.json) do (
        set line=%%a

        rem 提取 URL
        for /f "tokens=2 delims=:{" %%b in ("!line!") do (
            set url=%%b
            set url=!url:~1,-2!

            rem 执行 curl 命令
            curl -I -k https://111.229.132.28:!port!!url! >> !output_file!
        )
    )
    echo "脚本执行完成，结果已写入到 !output_file!"
)
echo "全部脚本执行完成"
