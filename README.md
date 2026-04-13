# AI Agent Benchmarking

## Overview

This project benchmarks different AI agent architectures on a QA task using SQuAD.

## Agents

* Basic (single-step)
* Multi-step
* RAG

## Dataset Description

* **Source**: SQuAD (Stanford Question Answering Dataset)
* **Type**: Extractive Question Answering
* **Size Used**: 1000 samples (validation split)

### Data Format

Each sample contains:

* Context (paragraph)
* Question
* Answer (text span)

### Preprocessing

* Selected first 1000 validation samples
* Extracted:

  * context
  * question
  * first ground truth answer
* No additional cleaning applied

## Metrics

* Exact Match
* F1 Score

## Results

* Basic: EM 67.8 | F1 76.9
* Multi-step: EM 60.8 | F1 70.18
* RAG: EM 50.9 | F1 59.36

## Setup Instructions

### 1. Clone repository

git clone https://github.com/arpitpaliwal007/agent-benchmark

### 2. Navigate to project folder

cd agent-benchmark

### 3. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

### 4. Install dependencies

pip install -r requirements.txt

---

## Running the Benchmark

### Architecture Comparison (Basic vs Multi-step)

python src/run_architecture.py

---

### RAG Benchmark (Retrieval-based Agent)

python src/run_rag.py

---

## Evaluation

### Evaluate Architecture Results

python evaluation/evaluate_architecture.py

### Evaluate RAG Results

python evaluation/evaluate_rag.py

---

## Visualization

### Generate performance plots

python evaluation/plot_results.py

This will generate:

* F1 score comparison graph
* Exact Match comparison graph

Saved in:
results/f1_comparison.png
results/em_comparison.png


