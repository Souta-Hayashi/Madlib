def madlib():
    company = input("Enter a car company: ")
    brand = input("Enter brand: ")
    litre = input("Enter engine capacity: ")
    cylinder = input("Enter number of cylinder: ")
    hp = input("Enter hp: ")
    torque = input("Enter torque: ")

    madlib = f"I have a/an {company} {brand}. It is {litre}L, twin turbo, V{cylinder}, with {hp}hp and {torque} Nm of torque."

    print(madlib)