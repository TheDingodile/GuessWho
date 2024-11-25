def plot_heatmap(ax, data, title, xlabel, ylabel, n):
    """Plot a heatmap with values overlayed."""
    cax = ax.imshow(data, cmap="viridis", interpolation="nearest", aspect="auto")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(range(1, n + 1))
    ax.set_yticklabels(range(1, n + 1))
    ax.invert_yaxis()
    for i in range(n):
        for j in range(n):
            value = data[i, j]
            ax.text(j, i, f"{value:.2f}", ha="center", va="center", fontsize=8, 
                    color="white" if value > 0.5 else "black")
    return cax