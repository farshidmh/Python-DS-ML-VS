from movie_recommender.recommender import MovieRecommender
from flask import Flask, jsonify, request

app = Flask(__name__)

recommender = MovieRecommender(dataset_path="../../dataset/movies_metadata.csv", sim_file="cosine_sim.npy")


@app.route('/', methods=['GET'])
def recom():
    title = request.args.get('title')

    try:
        a = recommender.get_recommendations(title, num_recommendations=5)
        return jsonify({'recomm': a})
    except ValueError as e:
        return jsonify({'error': str(e)})



app.run(debug=True)