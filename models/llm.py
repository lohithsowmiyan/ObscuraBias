from transformers import AutoModel, AutoTokenizer
import torch

class LLM:
    def __init__(self, args, **kwargs):
        self.temperature = args.temperature
        self.max_new_tokens = args.max_new_tokens
        self.model_name = args.llm_path


        self.tokenzier = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModel.from_pretrained(
            args.llm_path,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            device_map = "auto")


    @property
    def device(self):
        

    def __repr__(self):
        return f"model : {self.model_name}, temperature : {self.temperature}, running_on : {"GPU" if torch.cuda.is_available() else "CPU"}"

    def inference(self, samples):

        responses = []
        for sample in samples:
            inputs = tokenizer(sample, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
            outputs = model.generate(
                **inputs, 
                max_new_tokens=self.max_new_tokens,  # Adjust as needed
                temperature=self.temperature,
                top_p=0.8,
                do_sample=True
            )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            responses.append(response)

        return responses
