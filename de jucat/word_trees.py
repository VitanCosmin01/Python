import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "I love Python Coding because Python is easy to learn and simple!"

wordcloud = WordCloud(width=900, height=800).generate(text=text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Tree')
plt.show()
