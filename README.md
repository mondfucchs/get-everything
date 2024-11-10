'Get Everything' is a Python functions package with input-derivate functions. All them are listed and explained below:

get_int(prompt):

is a function which ONLY accepts integer values from the user. As we shall see, all 'get' functions have the 'prompt' argument: same as in 'input', the 'prompt' argument is going to be shown to the user. For example:

    print('Calculator:')
    n1 = get_int('Type the first number: ')
    n2 = get_int('Type the second number: ')

    print(f'{n1 + n2}')



    => next function



get_float(prompt):

Similarly to get_int, it only receive float values. Therefore, it accepts integer values too.



    => next function



get_these(element1, element2, prompt):

is a function which ONLY accepts one of the two elements provided as arguments. For example:

    answer = get_these('S', 'N', 'Do you want to finish your order [S/N]?')

get_these accepts lowercase and uppercase inputs.
Hence, if the use types 'n' or 's', the function will accepts those values nonetheless they aren't exactly equalt to 'S' and 'N', the 'element1' and 'element2'.



    => next function



get(element, prompt):

The simplest of all the functions, it onlt accepts the 'element' argument.
Although it can appear to be not quite useful, it can be used when you need a, for example, a key of the user:

    pass = get('011546A', 'Type the code sent to your e-mail: ')

Differently of 'get_these', 'get' only accepts the exact same configuration of uppercase and lowercase.



    = end of the functions =



Feel totally free to use these functions wherever you want.
Nowadays the repository is been managed by 'mondfucchs'.