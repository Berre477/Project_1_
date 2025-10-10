from math import sqrt


def ecart_type(list_of_numbers):
    pop_mean = sum(list_of_numbers) / len(list_of_numbers)
    list_op = []
    for x in list_of_numbers:
        list_op.append(((x - pop_mean) ** 2))
    sum_of_value = sum(list_op)
    return sqrt((sum_of_value / len(list_of_numbers)))


def is_correct(PRNG):
    prng1 = PRNG(33, 11)
    # verifier la valeur limite superieur
    for _ in range(100):
        nombre = prng1.next_int()
        if nombre >= 11 or nombre < 0:
            return False

    # Tester si le prng donne meme valeur
    prng2 = PRNG(33, 11)
    prng3 = PRNG(33, 11)
    list_prng2 = [prng2.next_int() for _ in range(100)]
    list_prng3 = [prng3.next_int() for _ in range(100)]
    if list_prng2 != list_prng3:
        return False

    # Verifier sur differente seed
    prng4 = PRNG(12, 11)
    prng5 = PRNG(32, 11)
    list_prng4 = [prng4.next_int() for _ in range(100)]
    list_prng5 = [prng5.next_int() for _ in range(100)]

    if list_prng4 == list_prng5:
        return False

    # verifie pour ecart type et seed de 3
    prng_de_seed_3 = PRNG(3, 11)
    valeur_seed_3 = [prng_de_seed_3.next_int() for _ in range(100)]
    value = [prng1.next_int() for _ in range(100)]
    ecart = ecart_type(value)
    ecart_seed_3 = ecart_type(valeur_seed_3)
    if ecart < 3.2:
        return False
    if ecart_seed_3 < 3.2:
        return False

    # Si passe toute les vérifications
    return True
