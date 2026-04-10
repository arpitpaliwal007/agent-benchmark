import pandas as pd
import evaluate

df = pd.read_csv("results/rag_results.csv")

metric = evaluate.load("squad")

def compute_scores(col):
    predictions = []
    references = []

    for i, row in df.iterrows():
        predictions.append({
            "id": str(i),
            "prediction_text": str(row[col])
        })

        references.append({
            "id": str(i),
            "answers": {
                "text": [str(row["true"])],
                "answer_start": [0]
            }
        })

    return metric.compute(predictions=predictions, references=references)

print("BASIC:", compute_scores("basic"))
print("RAG:", compute_scores("rag"))