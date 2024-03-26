# variable argumenta *args is a tuple refrence
# variable arguments **krwgs is dictionary reference

def great_people(*people: str):
    print(people)

    for i in people:
        print(f"Hello {i}")


great_people("Aman", "Atishi")


def people(**kwargs):
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])
    print(kwargs["address"])


people(name="anup", age= 14, address="Kanpur")