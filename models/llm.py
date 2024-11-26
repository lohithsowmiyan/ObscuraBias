from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

class LLM:
    def __init__(self, args, **kwargs):
        self.temperature = args.temperature
        self.max_new_tokens = args.max_new_tokens
        self.model_name = args.llm_path


        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        

    def __repr__(self):
        return f"model : {self.model_name}, temperature : {self.temperature}, running_on_gpu : {torch.cuda.is_available()}"

    def inference(self, samples, metrics):

        generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer, device=0 if torch.cuda.is_available() else -1)

        result = {}
        
        for treatment, rows in samples.items():
            responses = []
            for row in rows:
                response = generator(row, max_length=50, num_return_sequences=1)
                responses.append(response[0]['generated_text'])
                
            result[treatment] = [metrics.calc_toxicity(responses)]
            

        return result

    def infer_and_save(self, samples, metrics):

        generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer, device=0 if torch.cuda.is_available() else -1)

        data = []

        for treatment, contexts in samples.items():
            treatment_1 , treatment_2 = treatment.split("_")
            for context, rows in contexts.items():
                responses = []
                for row in rows:
                    response = generator(row, max_length = 50, num_return_sequences = 1)
                    data.append([row, treatment_1, treatment_2, context, metrics.calc_regard(response[0]['generated_text'], return_one = True), metrics.calc_toxicity(response[0]['generated_text'], return_one = True)])

        return data
                

