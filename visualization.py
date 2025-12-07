import matplotlib.pyplot as plt


def plot_comparison(linear_total, hungarian_total, optimized_total):

    labels = ["Linear", "Hungarian", "Hungarian + Greedy + Clustering"]
    costs = [linear_total, hungarian_total, optimized_total]

    fig, ax = plt.subplots(figsize=(6, 5))
    bars = ax.bar(labels, costs, color=["skyblue", "orange"])

    for bar, cost in zip(bars, costs):
        ax.annotate(
            f"{cost:.6f}",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
        )

    ax.set_ylabel("Total Cost / Execution Time")
    ax.set_title("Total Test Suite Cost Before and After Optimization")
    plt.tight_layout()
    plt.show()
