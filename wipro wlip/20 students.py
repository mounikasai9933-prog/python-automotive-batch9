 
students = [
    ("Ravi", "Kumar"),
    ("Sita", "Reddy"),
    ("Ravi", "Sharma"),
    ("Anil", "Verma"),
    ("Sita", "Patel"),
    ("Sunil", "Rao"),
    ("Anil", "Gupta"),
    ("Meena", "Iyer"),
    ("Kiran", "Das"),
    ("Pooja", "Singh"),
    ("Ramesh", "Naik"),
    ("Kiran", "Mehta"),
    ("Asha", "Nair"),
    ("Vijay", "Joshi"),
    ("Rahul", "Malhotra"),
    ("Neha", "Kapoor"),
    ("Asha", "Menon"),
    ("Ramesh", "Yadav"),
    ("Pooja", "Chopra"),
    ("Sunil", "Shetty")
]

# Dictionary to store unique first names
unique_students = {}

# Logic to maintain only one duplicate
for first_name, surname in students:
    if first_name not in unique_students:
        unique_students[first_name] = surname

# Display result
print("Students after removing duplicate first names:\n")
for name, surname in unique_students.items():
    print(name, surname)