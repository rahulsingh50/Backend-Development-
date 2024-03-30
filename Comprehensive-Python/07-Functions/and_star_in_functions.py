# standard arguments

def standard_arg(arg):
    print(arg) # both you can apply positional and keywords


# only positional arguments / after arguments
def pos_only_arg(arg1, arg2, /):
    print(arg1, arg2)


# only keywords arguments * before the arguments
def kwd_only_args(*, args1, args2):
    print(args1, args2)

# combined example standards, positionals, keywords arguments


def combined_example(pos_only, /, standard1, standard2, *, kwd_only):
    print(pos_only, standard1,standard2, kwd_only)


# if __name__ == '__manin__':
pos_only_arg(1, 2) # name=2 got error due to keywords args
kwd_only_args(args1=2, args2=3) # only give the keywords arguments
combined_example(1,2,standard2="Anup",kwd_only='Ram')




