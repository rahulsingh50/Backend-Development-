'''
3 way to access the modules

import random
from random import randint
from random import randint as rd


How to make a directory to python package just adding __init__.py file each directory

sing
    __init__.py
    -ml
        __init__.py
        -regression
           __init__.py
           linear.py

        -classification
           __init__.py
           logistic.py

And if the working directory of application is not parent folder of sing then you need to register folder 'sing' into PYTHONPATH environment variable.

For importing linear from sing folder you can use relative path:

from ml.regression import linear

and for calling function of linear file you can use:

linear.<*functionname*>(...)

'''




# import sample_package.sample_module as sm
# import sample_package.sample_module2 as sm2

# or
from test_package.sample_package import sample_module,sample_module2

sample_module.hello()
sample_module2.hello2()


# sm.hello()
# sm2.hello2()