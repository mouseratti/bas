# A module allows you to logically organize your Python
# code. Grouping related code into a module makes the code
# easier to understand and use. A module is a
# Python object with arbitrarily named attributes that you
# can bind and reference.

# Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

# The Python code for a module named aname normally resides
# in a file named aname.py. Here's an example of a simple
# module, support.py

def print_func( par ):
    print("Hello : ", par)
    return

# The import Statement
# You can use any Python source file as a module by
# executing an import statement in some other Python
# source file. The import has the following syntax −

# import module1[, module2[,... moduleN]
# When the interpreter encounters an import statement,
# it imports the module if the module is present in the search path.
# A search path is a list of directories
# that the interpreter searches before importing a module.
# For example, to import the module support.py,
# you need to put the following command at the top of the script −

import support

# Now you can call defined function that module as follows
support.print_func("Zara")
# When the above code is executed,
# it produces the following result −

# A module is loaded only once,
# regardless of the number of times it is imported.
# This prevents the module execution from happening over and over again
# if multiple imports occur.

# The from...import Statement
# Python's from statement lets you import specific attributes
# from a module into the current namespace.
# The from...import has the following syntax −
# from modname import name1[, name2[, ... nameN]]
# For example, to import the function fibonacci
# from the module fib, use the following statement −

from fib import fibonacci
# This statement does not import the entire module fib into
# the current namespace;
# it just introduces the item fibonacci
# from the module fib into the global symbol table of the importing module.

    # The from...import * Statement
# It is also possible to import all names from a module into the current namespace by using the following import statement −
# from modname import *
# This provides an easy way to import
# all the items from a module into the current namespace; however, this statement should be used sparingly.

# Locating Modules
# When you import a module, the Python interpreter searches for the module in the following sequences −

# The current directory.
# If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.

# If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.

# The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.

# The PYTHONPATH Variable
# The PYTHONPATH is an environment variable, consisting of a list of directories. The syntax of PYTHONPATH is the same as that of the shell variable PATH.
#
# Here is a typical PYTHONPATH from a Windows system −
#
# set PYTHONPATH = c:\python20\lib;
# And here is a typical PYTHONPATH from a UNIX system −
#
# set PYTHONPATH = /usr/local/lib/python
# Namespaces and Scoping
# Variables are names (identifiers) that map to objects.
# A namespace is a dictionary of variable names (keys)
# and their corresponding objects (values).
#
# A Python statement can access variables in a local namespace
# and in the global namespace.
# If a local and a global variable have the same name,
# the local variable shadows the global variable.
#
# Each function has its own local namespace.
# Class methods follow the same scoping rule as ordinary functions.
# Python makes educated guesses on whether variables are local or global.
# It assumes that any variable assigned a value in a function is local.
# Therefore, in order to assign a value to a global variable within a function,
# you must first use the global statement.
# # The statement global VarName tells Python that VarName is a global variable.
# Python stops searching the local namespace for the variable.
# For example, we define a variable Money in the global namespace.
# Within the function Money, we assign Money a value,
# therefore Python assumes Money as a local variable.
# However, we accessed the value of the local variable Money before setting it,
# so an UnboundLocalError is the result.
# Uncommenting the global statement fixes the problem.