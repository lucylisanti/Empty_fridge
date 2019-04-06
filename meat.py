meats = ['chicken', 'lamb', 'pork', 'beef', 'bacon']


str1 = 'chicken stew'


def veggie(string):

    val = []

    for meat in meats:
        if string.find(meat) == -1:
            val.append(True)
        else:
            val.append(False)

    print(all(val))









