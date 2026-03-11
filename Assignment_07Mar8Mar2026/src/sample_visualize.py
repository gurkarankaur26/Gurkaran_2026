
from get_embeddings import get_embedding
from visualize_words import visualize_pca_2d
words = ['cat', 'dog', 'bike', 'kitten', 'puppy', 'bicycle', 'aeroplane', 'helicopter', 'cow', 'wolf', 'lion', 'fighter jet']
embeddings = []
for i in words:
    embeddings.append(get_embedding(i))
visualize_pca_2d(embeddings, words)