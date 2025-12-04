def doh() -> list:

    return ["Homer: D'oh!" , "Marge: A Deer!", "Lisa: Female Deer"]



for line in doh():
    print(line)


print('----------- with using generator ---------------')


def doh2():
    yield "Home: D'oh!"
    yield "Marge: A Deer!"
    yield "Lisa: Female Deer"



for line in doh2():
    print(line)


# Any function containing yield is a generator function. Given this ability to go back
# into the middle of a function and resume execution, the next section looks like a logi‐
# cal adaptation.