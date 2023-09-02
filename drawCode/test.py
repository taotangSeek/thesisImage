import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# Example data
x = [1.8, 2.1, 2.4, 2.83]  # X-coordinates of the four positions
y = [2.5, 3, 2.6, 3.2]  # Y-coordinates of the four positions
features = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']  # Features of the four positions
colors = ['orange', 'lime', 'violet', 'deepskyblue']  # Colors for each feature
out_colors = ['navajowhite', 'lightgreen', 'plum', 'skyblue']  # Colors for each feature
ellipse_width = [1, 1.2, 1.5, 2]
ellipse_height = [0.7, 1.2, 1.5, 0.9]
ellipse_angle = [30, 90, 120, 50]
sizes = [100, 100, 100, 100]  # Sizes for each feature
markers = ['o', 's', '^', '*']  # Markers for each feature

# Plotting the scatter plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot colored circles for the four positions
for i in range(4):
    # Plot scatter point with black edge color
    ax.scatter(x[i], y[i], c=colors[i], s=sizes[i], marker=markers[i], edgecolors='black', linewidths=1, label=features[i])

    # Create an Ellipse object
    ellipse = Ellipse((x[i], y[i]), width=ellipse_width[i], height=ellipse_height[i], angle=ellipse_angle[i],
                      facecolor=out_colors[i], alpha=0.5)  # Set alpha value for transparency

    # Add the ellipse to the plot
    ax.add_artist(ellipse)

    # # Plot scatter point at the center of the ellipse
    ax.scatter(x[i], y[i], c=colors[i], s=sizes[i], marker=markers[i], edgecolors='black', linewidths=1)

# Set plot title and labels
ax.set_title('Scatter Plot with Features')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.xlim(1, 4)
plt.ylim(2, 4)

# Add legend
ax.legend()

# Show the plot
plt.show()