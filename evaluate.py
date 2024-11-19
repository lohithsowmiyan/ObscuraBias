from transformers import pipeline
from detoxify import Detoxify

class Metrics:
    def __init__(self):

        self.regard_pipe =  pipeline(
            "text-classification",
            model="lizenns/regard",
            tokenizer="lizenns/regard",
            return_all_scores=True
        )

        self.detoxify  =  Detoxify('original')


    def calc_regard(self, responses):
        scores = []
        for response in responses:
            scores = regard_pipeline(response)
            for result in scores:
                print(result['label'], result['score'])

    def calc_toxicity(self, responses):
        scores = self.detoxify.predict(response)
        print(scores)

