from g3kko import db
from datetime import date



class Transaction(db.Model):
    """Model for a Transaction

    Mapping for CSV import:
    date: Valuta
    text: Auftraggeber, Buchungstext, Verwendungszweck
    purpose: calculation from text
    currency: Waehrung
    value: Betrag
    shares: has to be updated by the user
    isin: calculation from text


    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    text = db.Column(db.Text, nullable=True)
    purpose = db.Column(db.String(128), nullable=True)
    value = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='EUR')
    shares = db.Column(db.Float, nullable=True)
    isin = db.Column(db.String(12), nullable=True)

    def value_per_share(self):
        return self.value/self.shares

    def __repr__(self):
        return '<Transaction %i %s %f>' % (self.id, self.date, self.text, self.value)
