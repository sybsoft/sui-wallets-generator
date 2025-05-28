# Sui Wallets Generator

Скрипт генерирует sui-кошельки в заданном количестве и экспортирует их в Excel
The script generates sui wallets in a given quantity and exports them to Excel

## Установка

### Windows:
```bash
cd путь\к\проекту
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### MacOS / Linux:
```bash
cd путь/к/проекту
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск

Вызываем команду:
```bash
python main.py
```

## Возможности

- ✅ Генерация кошельков с BIP39 мнемониками
- ✅ Экспорт в Excel формат
- ✅ Поддержка ED25519 схемы подписи
- ✅ Совместимость с официальным Sui кошельком

## Требования

Смотрите файл `requirements.txt` для полного списка зависимостей.
