@echo off


set dir = E:\Current\00_Project\COMNET\COMNET_PJ

rem 定义输出文件
set output_file= !dir!\test.txt
curl -I -k https://111.229.132.28:8443 >> output_file
echo "done test 8443"