'Get Everything' is a Python functions package with input-derivate functions. All them are listed and explained below:

```get_int(prompt):```

is a function which ONLY accepts integer values from the user. As we shall see, all 'get' functions have the 'prompt' argument: same as in 'input', the 'prompt' argument is going to be shown to the user. For example:

    print('Calculator:')
    n1 = get_int('Type the first number: ')
    n2 = get_int('Type the second number: ')

    print(f'{n1 + n2}')

```get_float(prompt):```

Similarly to get_int, it only receive float values. Therefore, it accepts integer values too.

```get_these(element1, element2, prompt):```

is a function which ONLY accepts one of the two elements provided as arguments. For example:

    answer = get_these('S', 'N', 'Do you want to finish your order [S/N]?')

get_these accepts lowercase and uppercase inputs.
Hence, if the use types 'n' or 's', the function will accepts those values nonetheless they aren't exactly equalt to 'S' and 'N', the 'element1' and 'element2'.

```get(element, prompt):```

The simplest of all the functions, it onlt accepts the 'element' argument.
Although it can appear to be not quite useful, it can be used when you need a, for example, a key of the user:

    pass = get('011546A', 'Type the code sent to your e-mail: ')

Differently of 'get_these', 'get' only accepts the exact same configuration of uppercase and lowercase.

```get_this(_type: type, prompt: str, args: tuple[Any] = None, kwargs: dict[str, Any] = None):```

The most complex of all the functions. Takes a custom class `_type`. It takes inputs from the user, attempts to construct `_type` with the first argument being user input, the other arguments being `args` and `kwargs`. If the constructor throws an error, ask the user for another input; otherwise, return the value obtained from the constructor.
```python
class Value:
    def __init__(self, val1, val2):
        self.value = val1 + val2

import functions
v = functions.get_this(Value, "Enter a prefix: ", args=('-test',))
```
```python
import functions
v = functions.get_this(complex, 'Enter a complex value: ')
```

    = end of the functions =

Feel totally free to use these functions wherever you want.
Nowadays the repository is been managed by 'mondfucchs'.