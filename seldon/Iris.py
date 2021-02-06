import numpy as np
import pickle
import pandas as pd


class Iris(object):

    def __init__(self):
        self.model = pickle.load(open('ml-bg.pkl', "rb"))

    def predict(self, X, features_names=None):
        user_data = pd.read_json("[{\"b_g\": \"425 0\", \"total_hits\": 0.10170139230422684}]")
        raw_predictions = self.model.predict(user_data)

        if raw_predictions is None:
            return []

        predictions = list(map(
            lambda k: {
                'brand_id': raw_predictions.brand[k],
                'gender': raw_predictions.gender[k],
                'score': raw_predictions.score[k],
                'liked': raw_predictions.liked[k]
            },
            raw_predictions.brand.keys()))

        return np.array(predictions)
