name = input('Enter your name: ')
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age.")
hometown = input('Enter your hometown: ')

print(name, age, hometown)
store = {
    'name': name,
    'age': age,
    'hometown': hometown,
}
print(store)

