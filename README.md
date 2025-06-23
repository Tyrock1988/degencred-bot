# ðŸ¤– DegenCred Bot

DegenCred is a fully autonomous **Telegram micro-lending bot** built for crypto communities. It integrates tightly with **CWallet-style bots** like `@gCodezWallet_bot` to monitor, manage, and automate decentralized trust, loan, and reputation systems.

---

## ðŸš€ Features

- ðŸ’¸ **Level-Based Microloans** with interest, credit scoring, and repayment tracking
- ðŸ‘¤ **User Reputation & Badge System** based on CWallet interactions
- ðŸ§  **Auto-detection of CWallet transactions** (tips, loans, fees, airdrops, slots)
- ðŸ› ï¸ **Admin dashboard** for loan management, alerts, overrides
- ðŸ”” **Real-time alert system** for all relevant Telegram messages
- ðŸ” Fly.io production-ready with secure env config

---

## ðŸ§± Tech Stack

- Python 3.11
- PostgreSQL (via asyncpg)
- FastAPI (for health monitoring)
- python-telegram-bot 20.x
- Fly.io (Docker-based deployment)

---

## ðŸ“¦ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourname/degencred-bot.git
cd degencred-bot
```

### 2. Configure Environment

Create a `.env` file:

```env
BOT_TOKEN=your-telegram-bot-token
DATABASE_URL=postgresql://...
ADMIN_IDS=6668510825,8055687062
BUSTER_USER_ID=6668510825
CWALLET_BOT_USERNAME=gCodezWallet_bot
GROUP_ID=-1002400589513
TRANSACTION_ALERT_THRESHOLD=1.00
```

> Never commit your `.env` file!

### 3. Run Locally

```bash
pip install -r requirements.txt
python main.py
```

### 4. Deploy to Fly.io

```bash
fly launch
fly secrets set BOT_TOKEN=... DATABASE_URL=... ...
fly deploy
```

---

## ðŸ“š Key Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome & verification |
| `/txalert` | (reply) Detect CWallet transaction |
| `/loan` | Request a loan |
| `/repay` | Repay active loan |
| `/reputation` | Show rep score |
| `/plusrep` | Give rep to other user |
| `/alerts` | Toggle transaction alerts |

---

## ðŸ§  Project Structure

```
.
â”œâ”€â”€ main.py                  # Entry point with FastAPI health server
â”œâ”€â”€ config.py                # Loads environment variables
â”œâ”€â”€ database.py              # PostgreSQL pool and schema setup
â”œâ”€â”€ bot/
â”‚   â”œâ”€â”€ handlers.py          # Telegram bot commands
â”‚   â””â”€â”€ cwallet_monitor.py   # Monitors messages from @gCodezWallet_bot
â”œâ”€â”€ utils/
â”‚   â”œâ”€â”€ transaction_processor.py
â”‚   â”œâ”€â”€ loan_utils.py
â”‚   â””â”€â”€ badge_manager.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ Dockerfile
â””â”€â”€ .env                     # (not committed)
```

---

## âš ï¸ License

This project is private and under development by **@GambleCodez**. Not for redistribution.

---
