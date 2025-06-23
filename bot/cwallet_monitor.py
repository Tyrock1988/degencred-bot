import re
from config import BUSTER_USER_ID
from utils.transaction_processor import process_cwallet_message

async def handle_cwallet_message(message, db_pool):
    if message.from_user.id != BUSTER_USER_ID:
        return

    content = message.text or message.caption or ""
    parsed = parse_cwallet_content(content)
    if parsed:
        await process_cwallet_message(parsed, message, db_pool)

def parse_cwallet_content(text):
    amount_match = re.search(r'\$?(\d+(?:\.\d{2})?)\s*(?:USD|USDT|\$)?', text)
    usernames = re.findall(r'@([a-zA-Z0-9_]{3,32})', text)
    hash_match = re.search(r'([a-fA-F0-9]{20,})', text)
    keywords = re.findall(r'(sent|received|tip|slots|airdrop|loan|repay)', text, re.IGNORECASE)

    if not amount_match or not usernames:
        return None

    return {
        "amount": float(amount_match.group(1)),
        "from_user": usernames[0] if usernames else None,
        "to_user": usernames[1] if len(usernames) > 1 else None,
        "hash": hash_match.group(1) if hash_match else None,
        "type": keywords[0].lower() if keywords else "transfer",
        "raw": text
    }
