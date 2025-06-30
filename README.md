# Crypto-Arbitrage-Finder
Crypto Arbitrage Finder is an asynchronous Python application that detects arbitrage opportunities by comparing cryptocurrency prices across multiple exchanges


---

## 📖 Описание / Description

**🇷🇺 Русский**  
**Crypto Arbitrage Finder** — асинхронное Python‐приложение, которое сравнивает цены криптовалют (например, BTC/USDT, ETH/USDT) на нескольких биржах (Binance, Coinbase) и показывает, где есть прибыльный арбитраж. Включает CLI (Typer), веб-интерфейс на FastAPI, Pydantic-валидацию, retry-логику и LRU-кеш.

**🇬🇧 English**  
**Crypto Arbitrage Finder** is an asynchronous Python application that compares cryptocurrency prices (e.g. BTC/USDT, ETH/USDT) across multiple exchanges (Binance, Coinbase) to reveal profitable arbitrage. It features a Typer CLI, FastAPI web UI, Pydantic validation, retry logic, and in-memory caching.

---

## 🚀 Features

- 🔹 Асинхронные HTTP-запросы через `httpx`  
- 🔹 Валидация и нормализация ответов с помощью `Pydantic`  
- 🔹 Retry-механика и LRU-кеширование запросов  
- 🔹 CLI на `Typer` (`crypto-arb find SYMBOLS`)  
- 🔹 Веб-интерфейс на `FastAPI` + Jinja2 (fetch + JS)  
- 🔹 Логирование через стандартный `logging`  
- 🔹 Юнит-тесты на `pytest`  

---

## 🛠 Installation

1. Клонируйте репозиторий  
   ```bash
   git clone https://github.com/your-username/crypto-arbitrage-finder.git
   cd crypto-arbitrage-finder
2. Создайте и активируйте виртуальное окружение

bash
python3 -m venv .venv
source .venv/bin/activate

Установите зависимости
3. pip install -r requirements.txt


