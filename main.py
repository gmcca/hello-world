city_list = open("cities")

search = input("Enter a County Name: ")

for line in city_list:
    if search in line:
        print(line)

print("Did this line work?")
