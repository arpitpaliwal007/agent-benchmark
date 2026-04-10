from datasets import load_dataset
from agent import agent_basic, agent_multistep
from tqdm import tqdm
import pandas as pd

dataset = load_dataset("squad", split="validation[:1000]")

results = []

for sample in tqdm(dataset):
    context = sample["context"]
    question = sample["question"]
    true_answer = sample["answers"]["text"][0]

    pred_basic = agent_basic(context, question)
    pred_multi = agent_multistep(context, question)

    results.append({
        "question": question,
        "true": true_answer,
        "basic": pred_basic,
        "multistep": pred_multi
    })

df = pd.DataFrame(results)
df.to_csv("results/architecture_results.csv", index=False)

print("Benchmark done!")