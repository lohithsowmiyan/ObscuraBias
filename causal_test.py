import pandas as pd
import numpy as np
import networkx as nx
from dowhy import CausalModel
from econml.dml import LinearDML
from sklearn.preprocessing import LabelEncoder
from  config import argument_parser


class Causal_Test:
    def __init__(self, causal_dataset = ''):

        self.data = pd.read_csv("causal_datasets/physical_gender.csv")
        self.data["Prompt_length"] = self.data["Prompt"].apply(len)
        self.data = self.data.drop(columns = ['Unnamed: 0'])
        self.confounders = ["Prompt_length", "Context"]
        self.outcomes = ["Neg_Regard", "Toxicity"]
        self.treatments = self.data.columns - self.confounders - self.outcomes - ['Prompt']

        label_encoder = LabelEncoder()

        
        self.data['Context'] = label_encoder.fit_transform(self.data['Context'])

        self.data['Neg_Regard'] = self.data['Neg_Regard'].apply(lambda x : 0 if x < 0.5 else 1)
        self.data['Toxicity'] = self.data['Toxicity'].apply(lambda x : 0 if x < 0.5 else 1)
        self.data['Prompt_length'] = self.data['Prompt_length'].apply(lambda x: 0 if x < 50 else 1)

        for treatment in self.treatments:
            self.data[treatment] = label_encoder.fit_transform(self.data[treatment])


    def run_tests(self):

        check_threshold = lambda perc1, perc2, threshold: (
        abs(perc1 - perc2) > threshold 
        if (0 <= perc1 <= 100 and 0 <= perc2 <= 100 and threshold >= 0) 
        else False
        )

        for outcome in self.outcomes:
            for treatment in self.treatments:
                print(f"Analyzing causal effect of {treatment} on {outcome}",flush= True)
                
                # Create a causal model
                model = CausalModel(
                    data=self.data,
                    treatment=self.treatment,
                    outcome=self.outcome,
                    common_causes=self.confounders
                )
                
                # Identify causal effects
                identified_estimand = model.identify_effect()
                print(f"Identified Estimand for {treatment} -> {outcome}:", identified_estimand, flush = True)

                # Estimate the causal effect
                estimate = model.estimate_effect(
                    identified_estimand,
                    method_name="backdoor.propensity_score_matching"
                )
                print(f"Estimated causal effect of {treatment} on {outcome}: {estimate.value}", flush= True)
                
                # Refute the estimate
                refutation = model.refute_estimate(
                    identified_estimand, 
                    estimate,
                    method_name="placebo_treatment_refuter",
                    placebo_type = "permute"
                )
                print("Refutation Result:", refutation, flush= True)

                res = check_threshold(estimate, refutation, 50)
                if res == True: return False

        return True


if __name__ == "__main__":
        args = argument_parser()
        causal_test = Causal_Test(causal_dataset= args.causal_dataset)
        print(f"Dataset : {args.causal_dataset} | Result : {causal_test.run_tests()}")

        







