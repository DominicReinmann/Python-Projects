
# simple programm that counts the numbers in given string and prints them


def get_my_name(name):
    counter = 0
    for letter in name:
        counter += 1
    return counter


name = "Dominic Reinmann"

print("Your name contains", get_my_name(name), "characters")


# instead of writing a function that ckecks if a word is in the string you can write it like example nr.2
def contains(big_string, little_string):
    for word in little_string and big_string:
        if little_string in big_string:
            return True
    else:
        return False


# example nr.2
def contains(big_string, little_string):
    return little_string in big_string


print("The answer is", contains("watermelon", "melon"))
