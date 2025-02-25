def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

def process_people(people_list):
    for person in people_list:
        person.greet()

def main():
    numbers = [10, 20, 30, 40, 50]
    avg = calculate_average(numbers)
    print(f"Average: {avg}")

    people = [
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie")
    ]

    process_people(people)

    data = {"a": 1, "b": 2, "c": 3}
    print(data["d"])

    text = "hello world"
    print(text.upperr())

if __name__ == "__main__":
    main()