import matplotlib.pyplot as plt

models = ["Basic", "Multi-step", "RAG"]
f1_scores = [76.9, 70.18, 59.36]
em_scores = [67.8, 60.8, 50.9]

# F1 graph
plt.figure()
plt.bar(models, f1_scores)
plt.title("F1 Score Comparison")
plt.savefig("results/f1_comparison.png")

# EM graph
plt.figure()
plt.bar(models, em_scores)
plt.title("Exact Match Comparison")
plt.savefig("results/em_comparison.png")