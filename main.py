# Section 1 - Complete by Komalpreet Kaur

def calculate_density(objects):
    density_dict = {}
    for key, (mass, volume) in objects.items():
        density = mass / volume
        # To round to 3 decimal places
        density_dict[key] = round(density, 3)
    return density_dict

# Creating Original Dictionary
original_dict = {
    "Box1": (433, 200),
    "Box2": (350, 120),
    "Box3": (289, 123),
    "Box4": (430, 250),
    "Box5": (350, 200)
}

# Calculating new dictionary with densities using a function
new_dict = calculate_density(original_dict)

# To view Output
print("\nOriginal Dictionary:\n", original_dict)
print("\nNew Dictionary with density:\n", new_dict)
print("\n")