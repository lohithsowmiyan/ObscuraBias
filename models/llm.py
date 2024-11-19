from transformers import AutoModel, AutoTokenizer

class LLM:
    def __init__(self, args, **kwargs):
        self.temperature = args.temperature
        self.max_new_tokens = args.max_new_tokens
        self.model_name = args.llm_path

        
        if args.use_gpu:
            kwargs = {
                "max_memory": {i: f'{size}GiB' for i, size in enumerate(args.max_memory)},
                "device_map": "auto",
                "revision": "main",
            }

        self.tokenzier = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(
            args.llm_path,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            **kwargs)


    @property
    def device(self):
        

    def __repr__(self):
        return f"model : {self.model_name}, temperature : {self.temperature}, running_on : {"GPU" if args.use_gpu else "CPU"}"

    def inference(self, input):
