import numpy as np
def cosine_similarity(A, B):
    dot_product_AB = np.dot(A, B)

    # Calculate the magnitudes |A| and |B|
    magnitude_A = np.linalg.norm(A)
    magnitude_B = np.linalg.norm(B)

    # Calculate the cosine similarity
    cosine_similarity = dot_product_AB / (magnitude_A * magnitude_B)
    return cosine_similarity