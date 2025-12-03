# Import required libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = """Data Science uses Python for visualization, 
machine learning, and analysis. Visualization helps 
understand patterns and trends easily."""

# Create a Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the Word Cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud Example')
plt.show()
