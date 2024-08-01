from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

def generate_board():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    for r in range(9):
        if board[r][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

board = generate_board()

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/submit', methods=['POST'])
def submit():
    global board
    row = int(request.form['row'])
    col = int(request.form['col'])
    num = int(request.form['num'])
    if is_valid(board, row, col, num):
        board[row][col] = num
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
