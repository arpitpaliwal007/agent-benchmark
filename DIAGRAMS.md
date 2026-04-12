# Architecture Diagram

Basic QA:
Context → QA Model → Answer

Multi-step:
Context → Chunking → QA per chunk → Best Answer

RAG:
Context → Chunking → TF-IDF Retrieval → QA Model → Answer



# Pipeline

Dataset → Agent → Prediction → Evaluation → Results
