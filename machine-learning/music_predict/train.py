import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

df_m = pd.read_csv("../../dataset/music_1k.csv")
df_m.sort_values(by='age', inplace=True)
features = ['age', 'gender']
target = ['genre']
X = df_m[features]
y = df_m[target]
numeric_features = ['age']
categorical_features = ['gender']
prep = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
    ]
)

clf = Pipeline(
    [
        ('preprocessor', prep),
        ('classifier', DecisionTreeClassifier())
    ]
)

clf.fit(X, y)
joblib.dump(clf, 'music_genre_model.joblib')
