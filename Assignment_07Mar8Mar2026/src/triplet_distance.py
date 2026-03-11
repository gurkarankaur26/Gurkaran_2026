from get_embeddings import get_embedding
from calculate_distance import calculate_distance
from draw_triangle import draw_triangle
def triplet_distance(a, b, c, model='text-embedding-3-small'):
    ae = get_embedding(a)
    be = get_embedding(b)
    ce = get_embedding(c)
    dab = calculate_distance(ae, be)
    dac = calculate_distance(ae, ce)
    dbc = calculate_distance(be, ce)
    print(f"{a} <> {b}: {dab}")
    print(f"{a} <> {c}: {dac}")
    print(f"{b} <> {c}: {dbc}")
    draw_triangle(dab, dbc, dac, a, b, c)
    


#triplet_distance('Fever', 'Temperature', 'Favour', )
triplet_distance('The product is amazing', 'positive', 'negative')