from datasets import load_dataset
from agent import agent_basic, agent_rag
from tqdm import tqdm
import pandas as pd

dataset = load_dataset("squad", split="validation[:1000]")

results = []

for sample in tqdm(dataset):
    context = sample["context"]
    question = sample["question"]
    true_answer = sample["answers"]["text"][0]

    pred_basic = agent_basic(context, question)
    pred_rag = agent_rag(context, question)

    results.append({
        "question": question,
        "true": true_answer,
        "basic": pred_basic,
        "rag": pred_rag
    })

df = pd.DataFrame(results)
df.to_csv("results/rag_results.csv", index=False)

print("RAG benchmark done!")