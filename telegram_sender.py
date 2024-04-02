from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send_to_telegram():
    content = request.json
    api_token = content.get('TELEGRAM_TOKEN')
    chat_id = content.get('TELEGRAM_CHANNEL')
    text = content.get('message')

    if not all([api_token, chat_id, text]):
        return jsonify({'error': 'Missing data'}), 400

    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': text})
        return jsonify({'response': response.text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
