@echo off
setlocal enabledelayedexpansion

curl -k https://111.229.132.28/speed-test-100KB.png --output speed-test-100KB.png
curl -k https://111.229.132.28/speed-test-1MB.png --output speed-test-1MB.png
curl -k https://111.229.132.28/speed-test-5MB.png --output speed-test-5MB.png

echo "All Done"
