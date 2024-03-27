# List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]


# Function to capitalize each name
def capitalize(name):
    return name.capitalize()


# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print(capitalized)

######################################

exam_scores = [85, 62, 95, 40, 78]


def is_passing(score):
    return score >= 70


status = list(map(is_passing, exam_scores))

print(status)

#############################

numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))

print(doubled)

################################
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)

##############################

products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}

# filtering products with prices less than 90
filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))

print(filtered_products)
