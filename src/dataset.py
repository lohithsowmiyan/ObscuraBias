import json

class Dataset():
    """
    Description : it is the custom dataset object, 
    loads the data from the json files into the desired format that would make it easier to work with during inferencing with large language models

    Arguments: (None)

    Methods: 
        1. load_data: is the member function to load the raw data from the json file
        2. get_promnpts: converts the raw data from the json file into desired format
        3. get_distributions: a dictionary containing the meta data about the data
    """

    def __init__(self):
        self.name = ""
        self.prompts = {}

    def __repr__(self):
        return f"DATASET_{self.name}"

    def load_data(self, path = 'datasets/physical_gender.json') -> bool:
        """
        Descriptoion : is the member function to load the raw data from the json file

        Paramaters:
            1. path: (str) is the path  to the specified json file containing the dataset
                Example : path = 'datasets/physical_gender.json'

        Returns: (bool) true if loaded otherwise false
        """
        try:
            with open(path, 'r') as file:
                dataset = json.load(file)
        
        except:
            print("cannot load from the the dataset")
            return False

        self.name = dataset['type']
        self._attributes = dataset['distinctions']
        self.dataset = dataset['data']

        return True
      

    def get_prompts(self) -> dict[str: dict[str: list]]:
        """
        Description : converts the raw data from the json file into desired format

        Parameters: None

        Returns:  (dict[str: dict[str: list]]) a dictionary containing the data which has key as all the treatmets (interesectional biases),  
        with values once again being dictionaries with contexts as key and list of prompts as values
        """

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


    def get_distribution(self) -> dict:
        """ 
        Description : a dictionary containing the meta data about the data

        Parameters: None

        Returns : a dicitonary with keys as treatmets and number of prompts per treatment as values
        """
        return {key : len(value) for key, value in self.prompts.items()}


    