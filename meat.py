meats = ['chicken', 'lamb', 'pork', 'beef', 'bacon']


def veggie(string):

    val = []

    for meat in meats:
        if string.find(meat) == -1:
            val.append(True)
        else:
            val.append(False)

    return all(val)














