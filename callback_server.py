from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def save_notification(product, amount, currency):
    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notifications (product, amount, currency) VALUES (?, ?, ?)', (product, amount, currency))
    conn.commit()
    conn.close()

@app.route('/callback', methods=['POST','GET'])
def handle_callback():
    data = request.json
    product = data.get('product')
    amount = data.get('amount')
    currency = data.get('currency')

    save_notification(product, amount, currency)

    return jsonify({'message': 'Callback received and processed successfully'})

if __name__ == '__main__':

    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            id INTEGER PRIMARY KEY,
            product TEXT,
            amount INTEGER,
            currency TEXT
        )
    ''')
    conn.close()

    app.run(host='0.0.0.0', port=5000, debug=True)
