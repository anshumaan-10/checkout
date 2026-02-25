import os
import sys
import time

import requests

PAYMENT_API_URL = os.environ.get("PAYMENT_API_URL", "http://payment-api:8080/transactions")
POLL_INTERVAL = 5
MAX_RETRIES = 3
RETRY_INTERVAL = 2

print("=" * 60)
print("Checkout Service Starting")
print("=" * 60)
print(f"Polling: {PAYMENT_API_URL}")
print(f"Interval: {POLL_INTERVAL}s (retry: {MAX_RETRIES}x @ {RETRY_INTERVAL}s)")
print("=" * 60)

consecutive_failures = 0

while True:
    try:
        response = requests.get(PAYMENT_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"[OK] Got {data['total_count']} transactions")
        consecutive_failures = 0
    except Exception as e:
        consecutive_failures += 1
        print(f"[ERROR] Attempt {consecutive_failures}/{MAX_RETRIES}: {e}")
        if consecutive_failures >= MAX_RETRIES:
            print("[FATAL] Max retries exceeded. Exiting.")
            sys.exit(1)
        time.sleep(RETRY_INTERVAL)
        continue
    time.sleep(POLL_INTERVAL)
