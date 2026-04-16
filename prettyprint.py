REDTEXT = "\033[31m" #Wrong
GREENTEXT = "\033[32m" #Success
YELLOWTEXT = "\033[33m" #Errors :(
BLUETEXT = "\033[34m" #I just like this color
RETURNDEFAULTCOLOR = "\033[0m" #Default term color
ROCKYOUHASHES = ['sha512', 'sha256', 'sha224', 'sha384'] #Random hashes for level 3 DICT
BARRIER = "#########################################" # I don't want to type my barrier out for block more than once
LOWERLETTERS = "abcdefghijklmnopqrstuvwxyz" #Lowercase letters for mask attacks
UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Uppercase letters for mask attacks
DIGITS = "1234567890" #Digits for mask attacks
MASK_FOUR_CHARS = "abc123" #Characters for mask level 4
SPECIAL_CHARS = '!"#$%&()*+,-./:;<=>?@^_{|}~' #Special characters for mask attacks
MASK_FIVE_CHARS = UPPERLETTERS + DIGITS + SPECIAL_CHARS # Characters for mask level 5

def block(message):
    width = max(len(message) + 4, len(BARRIER))
    barrier = "#" * width
    print(barrier)
    print(f'##{BLUETEXT}{message.center(width - 4)}{RETURNDEFAULTCOLOR}##')
    print(barrier)