import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

import warnings;

warnings.simplefilter('ignore')

dfm = pd.read_csv('../dataset/movies_metadata.csv', usecols=['tagline', 'overview', 'title'])

dfm['tagline'].fillna('', inplace=True)
dfm['overview'].fillna('', inplace=True)

dfm['description'] = dfm['overview'] + dfm['tagline']

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), stop_words='english')
tfid_matrix = tf.fit_transform(dfm['description'])

cosine_sim = linear_kernel(tfid_matrix, tfid_matrix)

cosine_sim_file = "cosine.sim.npy"

np.save(cosine_sim_file, cosine_sim)
