from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    anime_title = data.get('anime_title')

    if not anime_title:
        return jsonify({'error': 'No anime title provided'}), 400

    recommendations = get_recommendations(anime_title)

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
