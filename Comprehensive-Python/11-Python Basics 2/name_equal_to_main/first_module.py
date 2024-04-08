# if __name__ == __main__
# __name__ is special variable it set by compiler when run the module or script as a first task.
# Main use is check the condition when code run by original script/module or run by the import module
# if you wand some code not executed when module is import by other modules that code if __main__ == __name__ condition
import second_module


#second_module.second_module()  #  __name__ == second_module

def first_module():
    print(f"This is first module where __name__ == {__name__}")


if __name__ == '__main__':
    first_module()
