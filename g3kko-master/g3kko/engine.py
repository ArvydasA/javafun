from g3kko import app, db
from g3kko.api import Transaction
from flask import request





@app.route('/')
def hello():
    return 'g3kko engine is running'


@app.route('/transaction', methods=['GET', 'POST'])
def transaction_api():
    if request.method == 'POST':
        return 'transaction/id'
    else:
        return 'returns the api definition (CRUD operations) or stores a new tansaction with new id'


@app.route('/transaction/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def transaction(id):
    return 'returns a transaction with id %d' % id


@app.route('/transactions')
def transactions():
    return 'returns the api definition (listing, search and filter operation of more than one element)'


@app.route('/transactions/test')
def transactions_create_test_data():
    db.create_all()
    t1 = Transaction(value=100.24)
    t2 = Transaction(value=200.23)
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()
    r = Transaction.query.all()
    for t in r:
        print(t)
    return 'done.'

@app.route('/fund')
def fund():
    return 'returns the api definition of fund (CRUD operations)'
