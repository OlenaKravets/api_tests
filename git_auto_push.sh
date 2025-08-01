#!/bin/bash
set -e

echo "🔄 Очищаю попередні блокування Git..."
rm -f .git/index.lock
rm -f .git/refs/heads/main.lock
rm -f .git/HEAD.lock

echo "🧹 Очищаю кеш..."
git gc --prune=now
git fsck --full

echo "➕ Додаю всі зміни..."
git add -A

# Створюємо коміт з часом
commit_message="Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"
echo "💾 Створюю коміт: $commit_message"
git commit -m "$commit_message" || echo "⚠️ Немає змін для коміту"

echo "🚀 Виконую пуш у main..."
git push origin main --forc