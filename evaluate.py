from transformers import pipeline
import evaluate 

class Metrics:
    def __init__(self):
        self.regard = evaluate.load("regard", "compare")
        self.toxicity = evaluate.load("toxicity")

    def calc_regard(self, responses, precision = 2):
        regard_results = self.regard.compute(data = profession1_completions, references = profession2_completions)
        return round(regard_results['regard_difference']['negative'], 2)

    def calc_toxicity(self, responses):
        results = self.toxicity.compute(predictions=male_model_completions, aggregation="ratio")
        return results

    

