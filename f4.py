from f4_extra import BaseProvider, Provider


def seperator():
    return '=' * 100


base_pr = BaseProvider('имя', 1, 3)
print(base_pr.quality)

print(seperator())

pr_1 = Provider('name', 1, 3, True)
print(pr_1.quality)
print(pr_1.p_quality)

print(seperator())

pr_2 = Provider('nombre', 1, 3, False)
print(pr_2.quality)
print(pr_2.p_quality)

print(seperator())

pr_3 = Provider('nazwa', 0, 3, True)
print(pr_3.quality)
print(pr_3.p_quality)
