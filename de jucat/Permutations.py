from itertools import permutations


def allpermutations(str):
    permlist = permutations(str)

    for perm in list(permlist):
        print(''.join(perm))


if __name__ == "__main__":
    str = input("Enter you string: ")
    allpermutations(str)
