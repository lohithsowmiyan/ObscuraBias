from models.llm import LLM
from models import *
from metric import Metrics
from dataset import Dataset
import os
from  config import argument_parser
import pandas as pd


class BiasWrapper():
    """
        Descritpion : Gets in the input Dataset, Large Language Model, Metrics caches the LLM output for the prompts 
        and evaluate the responses using the metrics returning a new csv file of all the ouputs.

        Arguments: 
            1. dataset_path : (str) location of the dataset
            2. llm_model : (str) name as in the huggingface model cards
            3. metrics_list : (list[str]) name of the metrics to be used during the inference
            4. save : (bool) | (str) whether to save the inference output. saves in a default lcoation if the value is bool otherwise save in the given location
            5. args : (dict) additonal arguments from the config file (contains values like temparature, top_p , etc).

        Methods:
            1. get_data_wrapper: is the member function to perform the infernce for the user sepecified configurations
    """
    def __init__(self, dataset_path : str, llm_model : str, metrics_list : list, save : bool | str,  args : dict,   **kwargs):
        dataset_object = Dataset()
        dataset_object.load_data(path = args.dataset)
        self.prompts = dataset_object.get_prompts()
        self.distinctions = dataset_object.distinctions
        self.save = save
        
       
        args.llm_path = model_path[llm_model]
        self.model = LLM(args)
        self.metrics = Metrics()

    def get_data_wrapper(self):
       

        if(type(self.save) == str):

            save = self.save.split("/")[-1]
            
            directory_path = f'causal_datasets/{save[:-5]}.csv'
            print(directory_path)
            if os.path.exists(directory_path):
                print(f"File '{directory_path}' already exists. Passing...")
            else:
                data = self.model.infer_and_save(self.prompts, self.metrics)
                data = pd.DataFrame(data, columns = ['Prompt', self.distinctions[0], self.distinctions[1], 'Context', 'Neg_Regard', 'Toxicity'])
                data.to_csv(directory_path)
                

        
        
    






if __name__ == "__main__":

    args = argument_parser()
    bias_object = BiasWrapper(
        dataset_path = args.dataset,
        llm_model = args.llm_model_name,
        metrics_list = ['toxicity'],
        save = args.dataset,
        args = args,
        )

    print(bias_object.get_data_wrapper())

    
