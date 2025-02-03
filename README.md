
# **ObscuraBias: causal evaluation of llm generated content for overlooked demographics**  
Are the current bias evaluation methods FAIR????

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  


---

## **Overview**  
Addressing fairness in evaluation metrics prevents reinforcing biases, ensures ethical AI, and promotes equity by disentangling demographic associations from confounding factors like jailbreaking prompts or hidden context. Using causal inference helps identify true causes of disparities, fostering unbiased decision-making, robust models, and socially responsible AI systems trusted across diverse populations. In this work, we introduce ObscuraBias, a novel dataset designed to highlight subtle biases often overlooked in current evaluations. Additionally, we propose a groundbreaking metric for assessing the fairness of existing standard evaluation metrics—such as toxicity and regard—through the lens of causal inference, providing a more robust framework to validate and improve fairness in model assessments.


---

## **Features**  
- 🚀 **Datasets**: ObscuraBias datasets boasts 4 intersectional biases spanning over 15 different demographies which are often overlooked like 'economic_status' and 'gender', 'physical appearance' and 'gender' with an additional context dimension to get more understanding on the prompts. 
- 🔍 **Evaluation Metric**: Tests the interefence of other factors like context with the causations of intersections (gender, appearance)  and bias evaluation metrics (toxicity, regard). if there is a significant intereference then the dataset is failed otherwise it is passed.  


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

### **Experiment***
```bash
make -b demo
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
📧 **Email**: lohithsowmiyan1@gmail.com
📧 **Email**: mrityunjayjoshi.work@gmail.com
--- 
