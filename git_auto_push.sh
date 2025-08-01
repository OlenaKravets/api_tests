#!/bin/bash

echo "🔄 Очищаю можливі блокування Git..."
rm -f .git/index.lock
rm -f .git/refs/heads/main.lock
rm -f .git/HEAD.lock

echo "🔄 Додаю всі зміни..."
git add -A

commit_message="Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"
echo "💾 Створюю коміт: $commit_message"
git commit -m "$commit_message"

echo "🚀 Виконую примусовий пуш у main..."
git push origin main --force

if [ $? -eq 0 ]; then
    echo "✅ Пуш виконано успішно!"
    echo "⏳ Очікую генерацію Allure Report на GitHub Pages..."
    echo "🌐 Звіт буде доступний приблизно через 1–2 хвилини за посиланням:"
    echo "👉 https://olenakravets.github.io/api_tests/"
else
    echo "❌ Помилка під час пушу!"
fi
