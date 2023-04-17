import moogle

f = open("small_index.txt", "r")
lst = []
for line in f:
    strip = line.strip()
    list_strip = strip.split()
    lst.append(list_strip)
dict = moogle.dictionary_constructor(lst)
html = moogle.html_extractor("https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/")
for target in dict:
    for hit in html:
        if target == hit:
            dict[target] += 1
print(dict)

# print(dict)
# moogle.html_extractor("https://en.wikipedia.org/wiki/Palestinians")

