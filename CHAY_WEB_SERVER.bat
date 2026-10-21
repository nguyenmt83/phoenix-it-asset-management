@echo off
chcp 65001 >nul
echo ========================================================
echo   HE THONG QUAN LY THIET BI CNTT - PHOENIX GOLF RESORT
echo ========================================================
echo Dang mo ung dung tren trinh duyet tai http://localhost:8080 ...
start "" "http://localhost:8080"
echo May chu dang chay tai cong 8080. Nhan Ctrl + C de dung.
python -m http.server 8080
