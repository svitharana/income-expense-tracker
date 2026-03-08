import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

def save_transaction(transaction, date, account="default", currency="LKR"):
    file = project_root / "data" / account / f"{date}.json"
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.exists():
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = {
            "account_name": account,
            "currency": currency,
            "transactions": []
        }

    data["transactions"].append(transaction)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def get_transactions(date, account="default"):
    file = project_root / "data" / account / f"{date}.json"

    if file.exists():
        with open(file, "r") as f:
            data = json.load(f)
            return data["transactions"]
    else:
        return []
