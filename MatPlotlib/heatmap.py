# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data (5x5 matrix)
data = np.array([[65, 70, 75, 80, 85],
                 [80, 82, 78, 74, 70],
                 [90, 85, 88, 92, 95],
                 [60, 65, 62, 68, 72],
                 [78, 80, 84, 88, 90]])

# Create heatmap
sns.heatmap(data, annot=True, cmap='coolwarm')

# Add title
plt.title('Heatmap Example')
plt.xlabel('Subjects')
plt.ylabel('Students')

# Display
plt.show()
