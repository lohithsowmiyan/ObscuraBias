import argparse

def argument_parser():
    parser = argparse.ArgumentParser(description="BIAS")

    parser.add_argument("--seed", type=int, default=0)


    parser.add_argument("--llm_model_name", type=str, default='gpt-neo')
    parser.add_argument("--max_txt_len", type=int, default=512)
    parser.add_argument("--max_new_tokens", type=int, default=32)
    parser.add_argument("--temperature", type=int, default=0.7)


    parser.add_argument("--dataset", type =str, default = './datasets/physical_gender.json')


    args = parser.parse_args()
    return args