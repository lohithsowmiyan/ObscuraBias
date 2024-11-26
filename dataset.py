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
        self._attributes = dataset['distinctions']
        self.dataset = dataset['data']
       # self.contexts = [context for context in self.dataset['context']]

    def get_prompts(self):

        for dobj in self.dataset:
            context = dobj['context']
            for counter in dobj['prompts']:
                for key, value in counter.items():
                    print(value)
                    # Ensure key exists in self.prompts
                    if key not in self.prompts:
                        self.prompts[key] = {}
                    
                    # Ensure context exists under the current key
                    if context not in self.prompts[key]:
                        self.prompts[key][context] = []
                    
                    # Append the value to the context list
                    self.prompts[key][context].append(value)


        #print(self.prompts)
        return self.prompts

    @property
    def distinctions(self):
        return self._attributes


    def get_distribution(self):
        return {key : len(value) for key, value in self.prompts.items()}


    # @property
    # def contexts(self):
    #     return self.contexts


    