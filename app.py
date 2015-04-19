import os
from flask import Flask
from flask import request
app = Flask(__name__)

last_data = dict([['servo', '000'], ['left', '000'], ['right', '000']])

@app.route('/', methods = ['POST'])
def test():
	global last_data
	temp = dict(request.form)
	if 'left' in temp:
		last_data['left'] = temp['left'][0]
	if 'right' in temp:
		last_data['right'] = temp['right'][0]
	if 'servo' in temp:
		last_data['servo'] = temp['servo'][0]
	return str(last_data)

@app.route('/', methods = ['GET'])
def other_function():
	global last_data
	return str("*"+last_data['servo']+'F'+last_data['left'] + 'F' +last_data['right'])


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv('PORT', '5000')), host='0.0.0.0')
