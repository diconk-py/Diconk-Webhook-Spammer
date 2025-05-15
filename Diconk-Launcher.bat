@echo off
title Diconk Webhook Spammer

:: Run the script
python Diconk-Webhook-Spammer.py

:: Wait for user input if script exits (error or not)
echo.
echo [!] Script has exited. Press any key to close this window.
pause > nul
