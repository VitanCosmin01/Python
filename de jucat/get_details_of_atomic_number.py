import periodictable


# get details of an element by atomic number

atomic_no = int(input("Enter element atomic number: "))
element = periodictable.elements[atomic_no]
print("Atomic number: ", element.number)
print("Symbol: ", element.symbol)
print("Name: ", element.name)
