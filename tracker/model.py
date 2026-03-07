class Transaction:
    def __init__(self, t_id, t_type, amount, date, description):
        self.id = t_id
        self.type = t_type
        self.amount = amount
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "date": self.date,
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["type"],
            data["amount"],
            data["date"],
            data["description"]
        )