import numpy as np
from get_embeddings import get_embedding
from calculate_distance import calculate_distance

cat = get_embedding('cat')
dog = get_embedding('dog')
car = get_embedding('car')
bike = get_embedding('bike')
# Calculate distances between embeddings
distance_cat_dog = calculate_distance(cat, dog)
distance_cat_car = calculate_distance(cat, car)
distance_cat_bike = calculate_distance(cat, bike)
distance_bike_car = calculate_distance(bike, car)
distance_bike_dog = calculate_distance(bike, dog)

# Display distances
print(f"Distance between 'cat' and 'dog': {distance_cat_dog:.2f}")
print(f"Distance between 'cat' and 'car': {distance_cat_car:.2f}")
print(f"Distance between 'cat' and 'bike': {distance_cat_bike:.2f}")
print(f"Distance between 'bike' and 'car': {distance_bike_car:.2f}")
print(f"Distance between 'bike' and 'dog': {distance_bike_dog:.2f}")

# Compare distances
if distance_cat_dog < distance_cat_car and distance_cat_dog < distance_cat_bike:
    print("'cat' is closer to 'dog' than to 'car' or 'bike'.")

if distance_bike_car < distance_bike_dog and distance_bike_car < distance_cat_bike:
    print("'bike' is closer to 'car' than to 'dog' or 'cat'.")