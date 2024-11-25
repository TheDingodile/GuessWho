import numpy as np
import matplotlib.pyplot as plt
from plot import plot_heatmap
from math import ceil

n = 24 # amount of candidates in the game
# first dim: canditates left for me, second dim: canditates left you, third dim: turn
states = np.zeros((n, n, 2))
best_splits = np.zeros((n, n, 2))
states[0, :, 0] = 1 # if i have only 1 candidate and its my turn, i win
states[:, 0, 1] = 0 # if you have only 1 candidate and its your turn, i lose
states[:, 0, 0] = 1/np.arange(1, n+1) # if you have only 1 candidate and its my turn, i guess and win with probability 1/n
states[0, :, 1] = 1 - 1/np.arange(1, n+1) # if i have only 1 candidate and its your turn, you guess and win with probability 1-1/n

# i + 1 is the amount of candidates left for you, j + 1 is the amount of candidates left for me
for i in range(1, n): # amount of candidates left you
    for j in range(1, n): # amount of candidates left me
        # my turn
        my_options = [1/(j+1)]
        for k in range(1, j + 1): # k is the amount of candidates i take
            my_options.append(k/(j+1) * states[k-1, i, 1] + (1 - k/(j+1)) * states[j-k, i, 1])
        my_choice = np.max(my_options)
        # print(my_options)
        best_splits[j, i, 0] = np.argmax(my_options) + 1

        # your turn
        your_options = [1 - 1/(i+1)]
        for k in range(1, i + 1):
            your_options.append((k/(i+1) * states[j, k-1, 0] + (1 - k/(i+1)) * states[j, i-k, 0]))
        # your_options.append(states[j, (i+1)//2-1, 0])
        # your_options.append(int((i+1)/2)/(i+1) * states[j, int((i+1)/2), 0] + ceil((i+1)/2)/(i+1) * states[j, ceil((i+1)/2), 0])
        your_choice = np.min(your_options)
        best_splits[j, i, 1] = np.argmin(your_options) + 1

        states[j, i, 0] = my_choice
        states[j, i, 1] = your_choice

# print(best_splits[:,:, 0])
# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(20, 8))
titles = ["My Win Chance (My Turn)", "My Win Chance (Your Turn)"]

# Plot the heatmaps
for idx, ax in enumerate(axes):
    cbar = plot_heatmap(ax, states[:, :, idx], titles[idx], "Possibilities left you", "Possibilities left me", n)
    fig.colorbar(cbar, ax=ax, label="Win Chance")

plt.tight_layout()
plt.show()