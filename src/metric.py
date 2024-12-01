from transformers import pipeline
import evaluate 

class Metrics:
    '''

    Description : Returns a custom metric object that takes in lists of prompts and evaluates them by returning a
     score with the user specified metric Ex : 'toxicity' , 'regard' , 'honest' etc

    Arguments:
        1. scores : (list[str]) : list of metric names that is intended to evaluate model respones during inference

    Methods:
        Methods here are the list of evaluate using  funcions (ex cal_regard calculates the regard scores for all the mdoel respones)

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


    def calc_regard(self, responses,return_one = False,  precision = 2):

        regard_result = self.regard.compute(data = [responses])
        for rows in regard_result['regard'][0]:
            if rows['label'] == 'negative':
                return rows['score']

        


    def calc_toxicity(self, responses, return_one = False):
        results = self.toxicity.compute(predictions=[responses])
        return results['toxicity'][0]


        



