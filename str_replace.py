from re import findall as refindall
from re import sub as resub
from re import IGNORECASE as reIGNORECASE
from itertools import zip_longest


def replacing(what_to_replace: str, for_what: str, full_string: str) -> str:
    try:
        upper_list = [True if letter.isupper() else False for letter in refindall(what_to_replace, full_string, flags=reIGNORECASE)[0]]
    except IndexError:
        return "False"
    if all(upper_list):
        return resub(what_to_replace, for_what.upper(), full_string, flags=reIGNORECASE)

    replaced_word = ''.join(letter.upper() if is_upper else letter.lower()
                            for letter, is_upper in zip_longest(for_what, upper_list, fillvalue=False))

    return resub(what_to_replace, replaced_word, full_string, flags=reIGNORECASE)


test_string = 'testing is FUN part of each coding'
test_sting1 = 'FuN'
test_sting2 = 'fuN'

repl1 = "fun"
repl2 = "hell"
repl3 = "tt"
repl4 = "sun"

result = replacing(repl1, repl2, test_string)
result1 = replacing(repl1, repl2, test_sting1)
result2 = replacing(repl1, repl4, test_sting2)

print(result)
print(result1)
print(result2)
