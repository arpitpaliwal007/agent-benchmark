# AI Agent Benchmarking

## Overview

This project benchmarks different AI agent architectures on a QA task using SQuAD.

## Agents

* Basic (single-step)
* Multi-step
* RAG

## Metrics

* Exact Match
* F1 Score

## Results

* Basic: EM 67.8 | F1 76.9
* Multi-step: EM 60.8 | F1 70.18
* RAG: EM 50.9 | F1 59.36

## Run

pip install -r requirements.txt
python src/run_architecture.py
python evaluation/evaluate_architecture.py
