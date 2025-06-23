import asyncpg
import os
from config import DATABASE_URL

async def connect():
    return await asyncpg.create_pool(DATABASE_URL)

async def setup_db():
    pool = await connect()
    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username VARCHAR,
            total_rep INTEGER DEFAULT 0,
            level VARCHAR DEFAULT 'L1',
            verification_status VARCHAR DEFAULT 'unverified',
            join_date TIMESTAMP DEFAULT now(),
            badges TEXT,
            last_active TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS loans (
            loan_id VARCHAR PRIMARY KEY,
            user_id BIGINT,
            amount DECIMAL,
            interest_rate DECIMAL,
            total_due DECIMAL,
            status VARCHAR,
            request_date TIMESTAMP,
            due_date TIMESTAMP,
            approval_date TIMESTAMP,
            repayment_date TIMESTAMP,
            admin_id BIGINT,
            level VARCHAR
        );
        CREATE TABLE IF NOT EXISTS cwallet_transactions (
            transaction_id VARCHAR PRIMARY KEY,
            transaction_hash VARCHAR,
            from_username VARCHAR,
            to_username VARCHAR,
            amount DECIMAL,
            transaction_type VARCHAR,
            status VARCHAR,
            detected_at TIMESTAMP DEFAULT now(),
            processed_at TIMESTAMP,
            loan_id VARCHAR,
            message_text TEXT
        );
        """)
    return pool
