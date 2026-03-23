name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")


if age < 13:
    category = "a Child"
elif age >= 13 and age <= 19:
    category = "a Teenager"
elif age >= 20 and age <= 59:
    category = "an Adult"
else:
    category = "a Senior Citizen"


print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {category}.")
print(f"It's great that you enjoy {hobby}. Keep learning and growing!")
