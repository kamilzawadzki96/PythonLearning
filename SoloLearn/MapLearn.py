def odd(x):
    if x % 2 == 0:
        return x
    else:
        return "Tutaj byla liczba nie pasujaca do innych"

nums = [10,20,30,42,531,241]

print(list(map(odd, nums)))