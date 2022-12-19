import pickle
from sklearn.pipeline import Pipeline


class SomeModel:

    def __init__(self):
        self.model = None

    def predict(self, c) -> float:
        if self.model is None:
            raise ValueError('Load model first')

        negative_prob: float
        positive_prob: float
        negative_prob, positive_prob = self.model.predict_proba([message])[0]

        return positive_prob

    def load_pretrained_model(self):
        with open('./model_pipeline.pkl', "rb") as file:
            self.model: Pipeline = pickle.load(file)
