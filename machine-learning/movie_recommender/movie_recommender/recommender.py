import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
import os
import warnings;

warnings.simplefilter('ignore')


class MovieRecommender:
    def __init__(self, dataset_path, sim_file):
        self.__dataset_path = dataset_path
        self.__sim_file = sim_file
        self.__load_data()
        self.__load_or_compute_similarity()

    def __load_data(self):
        self.__dfm = pd.read_csv(self.__dataset_path, usecols=['tagline', 'overview', 'title'])
        self.__dfm['tagline'].fillna('', inplace=True)
        self.__dfm['overview'].fillna('', inplace=True)
        self.__dfm['description'] = self.__dfm['overview'] + self.__dfm['tagline']
        self.__indices = pd.Series(self.__dfm.index, index=self.__dfm['title']).drop_duplicates()

    def __load_or_compute_similarity(self):
        if os.path.exists(self.__sim_file):
            self.__cosine_sim = np.load(self.__sim_file)
        else:
            tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words='english')
            tfid_matrix = tf.fit_transform(self.__dfm['description'])
            self.__cosine_sim = linear_kernel(tfid_matrix, tfid_matrix)
            np.save(self.__sim_file, self.__cosine_sim)

    def get_recommendations(self, title,num_recommendations ):
        if title not in self.__indices:
            raise ValueError(f"Movie {title} not found in the dataset")

        idx = self.__indices[title]
        sim_scores = list(enumerate(self.__cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations + 1]

        movie_indices = [i[0] for i in sim_scores]

        return self.__dfm['title'].iloc[movie_indices].tolist()