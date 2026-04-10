import pandas as pd
import evaluate

df = pd.read_csv("results/architecture_results.csv")

metric = evaluate.load("squad")

def compute_scores(pred_col):
    predictions = []
    references = []

    for i, row in df.iterrows():
        predictions.append({
            "id": str(i),
            "prediction_text": str(row[pred_col])
        })

        references.append({
            "id": str(i),
            "answers": {
                "text": [str(row["true"])],
                "answer_start": [0]
            }
        })

    return metric.compute(predictions=predictions, references=references)

score_basic = compute_scores("basic")
score_multi = compute_scores("multistep")

print("\nBASIC:", score_basic)
print("MULTI-STEP:", score_multi)