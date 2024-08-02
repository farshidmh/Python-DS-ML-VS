import pandas as pd
import numpy as np
dfm = pd.read_csv('../dataset/movies_metadata.csv', usecols=['tagline', 'overview', 'title'])
indices = pd.Series(dfm.index, index=dfm['title']).drop_duplicates()
cosine_sim_file = "cosine.sim.npy"

cosine_sim = np.load(cosine_sim_file)

def get_recom(title, num_recommendations=10):
    if title not in indices:
        raise ValueError(f"Movie {title} not found in the dataset")

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]

    movie_indices = [i[0] for i in sim_scores]

    return dfm['title'].iloc[movie_indices]


m = get_recom("Jaws")
print(m)
