from models.llm import LLM
from models import *
from metric import Metrics
from dataset import Dataset
import os
from  config import argument_parser


def main(args):

    dataset_object = Dataset()
    dataset_object.load_data(path = args.dataset)
    prompts = dataset_object.get_prompts()
    args.llm_path = model_path[args.llm_model_name]
    model = LLM(args)
    metrics = Metrics()
    result = model.inference(prompts, metrics)
    print(result)
    






if __name__ == "__main__":

    args = argument_parser()
    main(args)
