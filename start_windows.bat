@echo off
chcp 65001 >nul
clear

echo ===========================================
echo 🦝 ЗАПУСК СИСТЕМЫ ЕНОТА... ПРОВЕРКА ОЗУ... 
echo ===========================================

:: 1. Проверяем, установлен ли вообще python в Windows
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python не обнаружен на вашем компьютере Windows!
    echo ⏳ Запускаю скрытую установку официального Python через Winget...
    
    :: Команда принудительной тихой установки стабильного Python из репозитория Microsoft
    winget install --id Python.Python.3.11 --exact --silent --accept-source-agreements --accept-package-agreements
    
    echo ✅ ИНСТАЛЛЯЦИЯ ЗАВЕРШЕНА! Перезапустите этот файл.
    pause
    exit
) else (
    echo ✅ Python обнаружен в системе. Синхронизирую контур...
)

:: 2. Ультимативный пуск нашей игры v1.4 прямо в консоли Windows
python text_rpg_roguelike.py

echo.
echo ===========================================
echo 🎮 Сессия завершена. Нажмите любую клавишу...
echo ===========================================
pause
