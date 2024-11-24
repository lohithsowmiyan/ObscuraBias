from models.llm import LLM
from models import *
from metric import Metrics
from dataset import Dataset
import os
from  config import argument_parser


class BiasWrapper():

    def __init__(self, dataset_path : str, llm_model : str, metrics_list : list, args : dict,  **kwargs):
        dataset_object = Dataset()
        dataset_object.load_data(path = args.dataset)
        self.prompts = dataset_object.get_prompts()
       
        args.llm_path = model_path[llm_model]
        self.model = LLM(args)
        self.metrics = Metrics()

    def get_data_wrapper(self):

        return self.model.infer_and_save(self.prompts, self.metrics)
        
    






if __name__ == "__main__":

    args = argument_parser()
    bias_object = BiasWrapper(
        dataset_path = args.dataset,
        llm_model = args.llm_model_name,
        metrics_list = ['toxicity'],
        args = args,
        )

    print(bias_object.get_data_wrapper())

    
