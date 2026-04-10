# Benchmark Report

## 1. Experiment Setup

* Model: DistilBERT (distilbert-base-cased-distilled-squad)
* Dataset: SQuAD
* Samples: 1000
* Task: Extractive Question Answering

### Agents:

1. Basic Agent (single-step)
2. Multi-step Agent (chunk-based)
3. RAG Agent (TF-IDF retrieval)

---

## 2. Metrics

* **Exact Match (EM)**: Measures exact string match
* **F1 Score**: Measures overlap between predicted and true answer

---

## 3. Results

| Model      | Architecture   | Exact Match | F1 Score |
| ---------- | -------------- | ----------- | -------- |
| Basic      | Single-step QA | 67.8        | 76.9     |
| Multi-step | Chunk-based QA | 60.8        | 70.18    |
| RAG        | Retrieval + QA | 50.9        | 59.36    |

---

## 4. Insights

* The basic agent performs best due to full context availability.
* Multi-step agent suffers from context fragmentation.
* RAG performance is limited by TF-IDF retrieval quality.
* Retrieval accuracy directly impacts overall performance.

---

## 5. Trade-offs

| Factor      | Basic | Multi-step | RAG    |
| ----------- | ----- | ---------- | ------ |
| Accuracy    | High  | Medium     | Low    |
| Speed       | Fast  | Slow       | Medium |
| Scalability | Low   | Medium     | High   |

---

## 6. Conclusion

* Single-step QA is best for structured datasets like SQuAD.
* RAG is more suitable for large-scale real-world applications.
* Retrieval quality is the key factor for improving RAG systems.
