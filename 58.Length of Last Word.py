def length_of_last_word(stroka: str) -> int:
    # if stroka[-1] == ' ':
    #     new_str = stroka.strip(' ')
    #     stroka2 = new_str.split(' ')
    #     length = len(stroka2[-1])
    #
    #     return length
    # return len(stroka.split(' ')[-1])
    return len(stroka.split()[-1])


print(length_of_last_word('ghbdtn o fdf d fd ffffff                    '))
