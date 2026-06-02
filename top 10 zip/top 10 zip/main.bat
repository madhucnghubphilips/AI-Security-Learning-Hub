@echo off
setlocal

echo ============================================
echo  Starting all LLM Demo Apps
echo ============================================

set ROOT=%~dp0

start "LLM01-02"   cmd /c call "%ROOT%LLM01-02\start_1.bat"
start "LLM03-04"   cmd /c call "%ROOT%LLM03-04\start_2.bat"
start "LLM05-06"   cmd /c call "%ROOT%LLM05-06\start_3.bat"
start "LLM07-LLM10" cmd /c call "%ROOT%LLM07-LLM10\start_4.bat"

echo.
echo [*] All groups launched. Press any key to exit.
pause

