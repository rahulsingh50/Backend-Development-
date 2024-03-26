def hello_people(name: str, age: int, greet: str = "Hello") -> int:
    print(f"{greet} My name is {name} and age {age}")
    return 0


hello_people(name="Rahul", age=14)


