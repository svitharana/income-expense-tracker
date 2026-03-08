from datetime import datetime
from tracker import storage
from tracker.model import Transaction


def generate_id(t_type, date):
    prefix = "in" if t_type == "income" else "ex"
    suffix = date.strftime("%Y%m%d%H%M%S")
    return f"{prefix}_{suffix}"


def create_transaction(t_type, amount, description):
    now = datetime.now()

    t_id = generate_id(t_type, now)
    date_str = now.strftime("%Y-%m-%d")
    transaction = Transaction(t_id, t_type, amount, date_str, description)

    year_month = now.strftime("%Y-%m")
    storage.save_transaction(transaction, year_month)
    return transaction

def get_transactions(date):
    transactions_dict = storage.get_transactions(date)
    transactions = [Transaction.from_dict(t) for t in transactions_dict]
    return transactions