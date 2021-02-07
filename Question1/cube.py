def get_volume(num):
    return num ** 3


x = int(input("Please enter in one edge of the cube to determine the volume: "))
print(f"The volume of the cube is {get_volume(x)}")
