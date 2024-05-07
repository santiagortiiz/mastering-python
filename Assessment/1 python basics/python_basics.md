Iterators - Intermediate
    Iterable: An object capable of returning its members one at a time.
        Sequence: List, tuple, str
        Non-sequence: dict, file like obj
        Custom: obj that implements sequence semantic.

        Implements iterable protocol (__iter__) or sequence protocol (__getitem__)
    Manual iteration: iter() and next()
    Iteration protocol.
        - Includes __iter__ and __next__ methods
    Iterable, Range iterable
        - An object capable of returning its members one at a time. Sequences / Non-sequences / Custom objects that implements sequence semantic (__iter__ or __getitem__)
    Generators - Intermediate
        - They are normally created by iterating over a function that yields values
    yield
    comprehensions vs generators
        - Set of concise looping and filtering instructions to create lists, sets and dictionaries.
    gen expressions
Dynamic typing - Advanced
    Strong and weak typing (Computer Science definitions, Python)
        - strong: variables require to declare a type when they are defined
        - weak: the type is defined at runtime because it can change
    Type Hinting
        - It's a way to indicate the type expected for a variable in a specific context.
        - Useful for documentation, legibility and manteinance of the code.
        - Useful for code static analysis.
Shared references - Advanced
    Weak references
        - Python objects include a reference count field, which counts how many objects are referencing it
        - allows you to create references to an object that will not increase the reference count.
Strings - Advanced
    Raw strings
        - do not scape characters
    Unicode and ASCII strings
        - ASCII: Standard code for information interchange, Assign numeric values to each character. (7bits)
        - Unicode: is a specification that aims to list every character used by human languages and give each character its own unique code
Dictionaries - Advanced
        - ordereddict: dict subclass that remembers the order entries were added
        - defaultdict: dict subclass that calls a factory function to supply missing values
        - hashable: Object that has a hash value which never changes during its lifetime (__hash__ and __eq__)
Sets - Advanced
    - Set: Unordered collection of distinct hashable objects (mutable — contents can be changed using add(), remove()...)
    - Frozenset: Inmutable set
    - Usages: Memberships, de-duplication, joint operation
Scopes in Python - Advanced
    global and nonlocal keywords (LEGB)
    - global: Is a declaration which holds for the entire current code block, the listed identifiers are to be interpreted as globals.
    - nonlocal: Causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals
    globals() and locals() functions: meaning, can we mutate them? Depends on the mutability of the variable.
        Para volver a enlazar variables encontradas fuera del ámbito más interno, se puede utilizar la declaración nonlocal

    - scopes: Is a textual region of a Python program where a namespace is directly accessible.
        - el alcance más interno, que es inspeccionado primero, contiene los nombres locales
        - los alcances de cualquier función que encierra a otra, son inspeccionados a partir del alcance más cercano, contienen nombres no locales, pero también no globales
        - el penúltimo alcance contiene nombres globales del módulo actual
        - el alcance más externo (el último inspeccionado) es el espacio de nombres que contiene los nombres integrados

Python standard library - Advanced
    pickle: binary serializer
    contextlib
    importlib
    pkgutil
    socket
Modules in Python - Advanced
    The module cache: sys.modules
    module reload, importlib