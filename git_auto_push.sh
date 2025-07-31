#!/bin/bash

# Автоматичний пуш усіх змін
echo "🔄 Додаю всі зміни до git..."
git add .

# Створюю коміт із поточною датою та часом
commit_message="Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"
echo "💾 Створюю коміт: $commit_message"
git commit -m "$commit_message"

# Пуш у гілку main
echo "🚀 Виконую пуш у main..."
git push origin main

# Перевірка статусу
if [ $? -eq 0 ]; then
    echo "✅ Пуш виконано успішно!"
else
    echo "❌ Помилка при пуші!"
fi
git reset
