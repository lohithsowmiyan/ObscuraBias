
# **ObscuraBias: causal evaluation of llm generated content for overlooked demographics**  
_A catchy one-liner that describes your project._

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Contributors](https://img.shields.io/github/contributors/your-repo.svg)](https://github.com/your-username/your-repo/graphs/contributors)  

---

## **Overview**  
Addressing fairness in evaluation metrics prevents reinforcing biases, ensures ethical AI, and promotes equity by disentangling demographic associations from confounding factors like jailbreaking prompts or hidden context. Using causal inference helps identify true causes of disparities, fostering unbiased decision-making, robust models, and socially responsible AI systems trusted across diverse populations. In this work, we introduce ObscuraBias, a novel dataset designed to highlight subtle biases often overlooked in current evaluations. Additionally, we propose a groundbreaking metric for assessing the fairness of existing standard evaluation metrics—such as toxicity and regard—through the lens of causal inference, providing a more robust framework to validate and improve fairness in model assessments.


---

## **Features**  
- 🚀 **Datasets**: Brief explanation.  
- 🔍 **Evaluation Metric**: Brief explanation.  


---

## **Getting Started**  

### **Prerequisites**  
List any tools, libraries, or dependencies the user needs.  
```bash
pip install -r requirements.txt
```

### **Installation**  
Step-by-step guide to set up the project.  
```bash
# Clone the repository
git clone https://github.com/lohithsowmiyan/ObscuraBias.git  

# Navigate to the project directory
cd ObscuraBias  

# Install dependencies
pip install -r requirements.txt
```

---

## **Usage**  

### **LLM inference**

```bash
python bias.py --dataset datasets/economic_gender.json --llm_model gpt-neo --temperature 0.9 
```

### **Causal Tests**
```bash
python causal_test.py --causal_dataset causal_datasets/economic_gender.csv
```


---

## **Contributing**  
We welcome contributions! Here's how you can help:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. Commit your changes (`git commit -m 'Add your feature'`).  
4. Push to the branch (`git push origin feature/your-feature`).  
5. Open a Pull Request.  

---

## **License**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  

---

## **Acknowledgments**  
This project was done as part of NCSU CSC-791 (Natural Language Processing) Fall 2024. 

---

## **Contact**  
For questions, feel free to reach out:  
📧 **Email**: your.email@example.com  
🐦 **Twitter**: [@your_handle](https://twitter.com/your_handle)  
🌐 **Website**: [your-website.com](https://your-website.com)

--- 
