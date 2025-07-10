@echo off
echo 🔥 API压测工具启动脚本
echo ==============================
echo.

echo 📦 检查依赖...
pip install -r requirements.txt

echo.
echo 🚀 开始压测...
echo.

python run_test.py

echo.
echo ✅ 压测完成！
pause 