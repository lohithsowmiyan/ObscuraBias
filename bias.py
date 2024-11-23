from models.llm import LLM
from models import *
from metric import Metrics
from dataset import Dataset
import os
from  config import argument_parser


class BiasWrapper():

    def __init__(self, dataset_path : str, llm_model : str, metrics_list : list, args : dict,  **kwargs):
        self.prompts = Dataset().load_data(path = dataset_path)
        args.llm_path = model_path[llm_model]
        self.model = LLM(args)
        metrics = Metrics()

    def get_data_wrapper():
        
    






if __name__ == "__main__":

    args = argument_parser()
    main(args)
