from transformers import pipeline
import evaluate 

class Metrics:
    '''
    '''
    def __init__(self, scores = ['toxicity']):
        self.scores = scores
        self.regard = evaluate.load("regard")
        self.toxicity = evaluate.load("toxicity")

    def calc_regard(self, responses, precision = 2):
        results = 0
        
        regard_results = self.regard.compute(data = responses)
        for rows in regard_results['regard']:
            for row in rows:
                if row['label'] == 'negative':
                    results += row['score']
        return results / len(responses)

    def calc_toxicity(self, responses):
        results = self.toxicity.compute(predictions=responses, aggregation="ratio")
        return results['toxicity_ratio']

        



