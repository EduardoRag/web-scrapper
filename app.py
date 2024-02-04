from flask import jsonify, make_response, Flask, request
from bs4 import BeautifulSoup
# from database import get_database
import requests
from app.database import get_database
from urllib.request import urlopen

db = get_database()
collection = db['websites']

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    getUrl = 'https://www.similarweb.com/pt/website/twitter.com'

    try:
        response = requests.get(getUrl, headers=headers).text
        soup = BeautifulSoup(response, 'html.parser')
        print(response)
        return jsonify({
            'title': 'title'
        })
    except Exception as e:
        return jsonify({ "error": f"Erro durante o scraping: { str(e) }" }), 500
    
@app.route('/api', methods=['POST'])
def hello():
    try:
        collection.insert_one({
            'title': 'teste',
            'description': 'teste',
            'image': 'teste'
        })
        return make_response(jsonify({'message': 'success'}), 201)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(host='localhost', port=5000, debug=True)