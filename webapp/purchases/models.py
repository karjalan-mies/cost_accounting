from webapp.db import db

class Purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String, nullable=False)
    store = db.Column(db.String, unique=True, nullable=False)
    cost = db.Column(db.DECIMAL, unique=False, nullable=False)
    date = db.Column(db.Date, nullable=False)
    comments = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'Purchases id: {self.id} at {self.date} cost = {self.url}'