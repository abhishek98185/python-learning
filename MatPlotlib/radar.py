import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Math', 'Science', 'English', 'History', 'Computer']
values = [85, 90, 75, 80, 95]

# Setup
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
values += values[:1]
angles = np.append(angles, angles[0])

# Plot
plt.polar(angles, values, 'o-', color='orange')
plt.fill(angles, values, color='orange', alpha=0.3)
plt.xticks(angles[:-1], labels)
plt.title('Radar Chart Example')

plt.show()
