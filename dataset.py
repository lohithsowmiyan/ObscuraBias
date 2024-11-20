import json

class Dataset():
    def __init__(self):
        self.name = ""
        self.prompts = {}

    def __repr__(self):
        return f"DATASET_{self.name}"

    def load_data(self, path = 'datasets/physical_gender.json'):

        with open(path, 'r') as file:
            dataset = json.load(file)

        self.name = dataset['type']
        self.dataset = dataset['data']
       # self.contexts = [context for context in self.dataset['context']]

    def get_prompts(self):

        for dobj in self.dataset:
            for counter in dobj['prompts']:
                for key, value in counter.items():
                    if key not in self.prompts.keys():
                        self.prompts[key] = []
                    self.prompts[key].append(value)

        return self.prompts


    def get_distribution(self):
        return {key : len(value) for key, value in self.prompts.items()}


    # @property
    # def contexts(self):
    #     return self.contexts


    