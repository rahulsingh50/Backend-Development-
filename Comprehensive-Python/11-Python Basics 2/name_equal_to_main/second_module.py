
print("This second module code is always running")


def second_module():
    print(f"This is run by second module where __name__ == {__name__}")  # __name__ == __main__


if __name__ == '__main__':
    second_module()

