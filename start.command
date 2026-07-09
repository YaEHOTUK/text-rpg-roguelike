#!/bin/bash

cd "$(dirname "$0")"

printf "\e[8;40;140t"

clear

echo "==========================================="
echo "🦝 ЗАПУСК СИСТЕМЫ ЕНОТА... ПРОВЕРКА ОЗУ... "
echo "==========================================="

if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 не обнаружен на вашем Маке!"
    echo "⏳ Запускаю скрытую установку менеджера Homebrew и Python..."

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    brew install python@3.11
    echo "✅ ИНСТАЛЛЯЦИЯ ЗАВЕРШЕНА! Пробую запустить игру..."
    sleep 2
else
    echo "✅ Python 3 обнаружен в системе. Синхронизирую контур..."
    sleep 1.5
fi

python3 text_rpg_roguelike.py

echo ""
echo "==========================================="
echo "🎮 Сессия завершена. Нажмите Enter для выхода..."
echo "==========================================="
read

