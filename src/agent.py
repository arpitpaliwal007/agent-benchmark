from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import torch

# Load model once
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")


# ---------------- BASIC AGENT ----------------
def agent_basic(context, question):
    inputs = tokenizer(question, context, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)

    start_idx = torch.argmax(outputs.start_logits)
    end_idx = torch.argmax(outputs.end_logits) + 1

    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_idx:end_idx])
    )

    return answer


# ---------------- IMPROVED AGENT ----------------
def clean_text(text):
    return text.strip().lower()

def agent_improved(context, question):
    context = context[:400]  # reduce noise
    answer = agent_basic(context, question)
    return clean_text(answer)


# ---------------- MULTI-STEP AGENT ----------------
def agent_multistep(context, question):
    chunks = [context[i:i+200] for i in range(0, len(context), 200)]

    best_answer = ""
    best_score = -1e9

    for chunk in chunks:
        inputs = tokenizer(question, chunk, return_tensors="pt", truncation=True)

        with torch.no_grad():
            outputs = model(**inputs)

        score = torch.max(outputs.start_logits).item()

        if score > best_score:
            start_idx = torch.argmax(outputs.start_logits)
            end_idx = torch.argmax(outputs.end_logits) + 1

            answer = tokenizer.convert_tokens_to_string(
                tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_idx:end_idx])
            )

            best_answer = answer
            best_score = score

    return best_answer

def agent_rag(context, question):
    # Step 1: split into chunks
    chunks = [context[i:i+200] for i in range(0, len(context), 200)]

    # Step 2: compute similarity
    vectorizer = TfidfVectorizer().fit(chunks + [question])
    vectors = vectorizer.transform(chunks + [question])

    question_vec = vectors[-1]
    chunk_vecs = vectors[:-1]

    similarities = cosine_similarity(question_vec, chunk_vecs).flatten()

    # Step 3: pick best chunk
    best_chunk = chunks[similarities.argmax()]

    # Step 4: run QA on best chunk
    return agent_basic(best_chunk, question)