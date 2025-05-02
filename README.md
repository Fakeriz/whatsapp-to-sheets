# whatsapp-to-sheets

Aplikasi Flask untuk menerima webhook Twilio WhatsApp, lalu mencatatnya ke Google Sheets via Apps Script.

## Struktur
- `app.py` – kode Flask webhook
- `requirements.txt` – dependency
- `Procfile` – konfigurasi Heroku

## Cara Deploy

1. `heroku create nama-aplikasi-anda`
2. `git push heroku master`
3. Atur Twilio Sandbox webhook ke:
