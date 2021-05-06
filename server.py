from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

turn = "X"

board = [["", "", ""], 
		 ["", "", ""], 
		 ["", "", ""]]

def check_win():
		return None

@app.route("/")
def home():

	winner = check_win()

	if winner:
		return render_template("winner.html", winner=winner)
	else:
		return render_template("home.html", player=turn)

@app.route("/move", methods=["POST"])
def move():

	global turn
	row = int(request.form['x'])
	col = int(request.form['y'])

	board[row][col] = turn

	if turn == "X":
		turn = "O"
	else:
		turn = "X"

	return "201"

@app.route("/board")
def getBoard():
	return jsonify(board)