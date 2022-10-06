# You have two lists [1, 2, 3, 4, 5], [5, 4, 3, 2, 1] . Create a list of tuples from this two lists and exclude all
# tuples of duplicated elements (for these examples - exclude (3, 3).
import itertools

list_1 = [1, 2, 3, 4, 5]
list_2 = [5, 4, 3, 2, 1]
out = list(itertools.product(list_1, list_2))

out_2 = list(zip(list_1, list_2))

for i in list_1:
    if (i, i) in out:
        out.remove((i, i))

    if (i, i) in out_2:
        out_2.remove((i, i))

print(out, out_2, sep='\n')