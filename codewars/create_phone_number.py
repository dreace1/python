#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
def create_phone_number(n:list):
    part1 = "".join(map(str, n[0:3]))
    part2 = "".join(map(str, n[3:6]))
    part3 = "".join(map(str, n[6:10]))

    return f"({part1})" + f" {part2}-" + f"{part3}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
