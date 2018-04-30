"""Main location for the Flask routes and methods."""

import sqlite3
from os.path import isfile

import depends  # NOQA
from mail import send_message

from flask import Flask, render_template, request, jsonify

if not isfile('comments.db'):
    db = sqlite3.connect('comments.db', check_same_thread=False)
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE comments(first_name TEXT, last_name TEXT, '
        'email_address TEXT, comment TEXT)'
    )
else:
    db = sqlite3.connect('comments.db', check_same_thread=False)
    cursor = db.cursor()

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    """The homepage of the website."""
    return render_template('index.html')


@app.route('/wonder')
def wonder():
    """The page for each wonder, generated dynamically."""
    return render_template('wonder.html')


@app.route('/api/post_comment', methods=['POST'])
def api_system():
    """The website API, used for posting and getting comments."""
    data = request.form
    fields = (
        data['first_name'], data['last_name'],
        data['email_address'], data['comment']
    )
    cursor.execute(
        'INSERT INTO comments(first_name, last_name, email_address, comment) '
        'VALUES(?, ?, ?, ?)', fields
    )
    db.commit()
    send_message(
        data['email_address'],
        'We have recieved your comment:\n'
        '"{0}"\nThanks for giving us feedback!'.format(
            data['comment']
        )
    )
    return jsonify(
        {'status': 'Comment added successfully!'}
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
