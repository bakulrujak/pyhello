from flask import Flask, jsonify

app = Flask('__name__')

@app.route('/')
@app.route('/index')
def index():
	message = {
				"firstname": "John",
				"lastname": "Williams",
				"message": "Hello World."
			}
	return jsonify(message)

if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=4000,
		debug=True
	)