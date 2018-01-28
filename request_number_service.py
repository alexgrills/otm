import random
import requests
from flask import Flask, jsonify
import json

app = Flask(__name__)

def one_to_one_million():
	return random.uniform(1,1_000_000)


@app.route('/get_a_number')
def get_a_number():
	number = one_to_one_million()
	response = requests.get('https://database_service/update_number?number={0}'.format(number))
	data = json.loads(response)
	if data['success']:
		return jsonify({
				'number': number
			})
	else:
		return jsonify({
				'number': -1
			})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)