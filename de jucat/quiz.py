def cube_of_number(n):
    return n ** 3


numbers = [1, 2, 3]
output = map(cube_of_number, numbers)
print(list(output))


def print_triungle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))


height = int(input("Enter the height of the triangle: "))
print_triungle(height)
