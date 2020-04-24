def lowercase_count(string):
    count = 0
    for character in string:
        if character.islower():
            count += 1
    return count

#################################

def abbrevName(name):
    first_last_name = name.split(" ")
    return first_last_name[0][1].upper() + "." + first_last_name[1][0].upper()


def abbrevName(name):
    return '.'.join(word[0] for word in name.split()).upper()
#################################
    
