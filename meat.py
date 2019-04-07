# meat

Pike
meats = ['chicken', 'lamb', 'pork', 'bacon', 'sausage', 'salami', 'prosciutto', 'jamon', 'ham', 'hotdog', 'bratwurst', 'beef', 'steak', 'brisket', 'veal', 'turkey', 'duck', 'liver', 'foie gras', 'fish', 'anchovy','basa','bass', 'bream','catfish','cod','dorade','eel','flounder','grouper','haddock','hake','halibut','herring','ilish','john dory','lamprey','lingcod','mackerel','mahi','mullet','pilchard','pollock','pomfret','pompano','salmon','sardine','shark','skate','snapper','sole','sprat','sturgeon','surimi','swordfish','tilapia','trout','tuna','turbot','whitefish','whiting']


def veggie(string):

    val = []

    for meat in meats:
        if string.find(meat) == -1:
            val.append(True)
        else:
            val.append(False)

    return all(val)














