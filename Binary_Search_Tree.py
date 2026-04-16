import math, base64
import prettyprint


#Step 1: Take an input string from the user

#Step 2: Create a binary search tree based on the parameters of the user for the children in each level of the tree. 
#Default will be a full binary tree with 2 children from every node, but the user can specify nodes that don't have children.
#
#Step 3: Encrypt the string by creating the BST encoding. 
# If the string entered is: ABCDEFG, then the binary search tree is:
#                   A
#                  / \
#                 B   C
#                / \ / \
#               D  E F  G
#And the encoding for the string "ABCDEFG" would be:
#              " DBEAFCG "
#
#
#The hardest part of this project is going to be creating a method of reversing the operations of the 
#BST encoding on trees that aren't full binary trees.


#First attempt at Full Binary (FB) Tree encoding


#Functions for ease of use and readability
def split_string(string):
    split_string = []
    for i in range(0, len(string)):
        split_string.append(string[i])
    return split_string

def my_base64(string, encode=True):
    if encode:
        encoded_bytes = base64.b64encode(string.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    else:
        decoded_bytes = base64.b64decode(string.encode('utf-8'))
        return decoded_bytes.decode('utf-8')

#FIXME: Iterate through the split string and print the characters in the order of the BST encoding.
def bst_encode(chars):
    lines = []
    index = 0
    level = 1
    while index < len(chars):
        line = ''.join(chars[index:index + level])
        lines.append(line)
        index += level
        level *= 2
    
    if lines:
        max_len = max(len(line) for line in lines)
        for line in lines:
            print(line.center(max_len))



#Main...
def main():
    prettyprint.block("Preparing the Binary Search Tree Encryption Module")
    #plaintext = input("Enter a string to encrypt: ")
    plaintext = "Try harder"
    encoded = my_base64(plaintext)

    print(f"Base64 Encoded: {encoded}")
    
    chars = split_string(encoded)
    bst_encode(chars)


if __name__ == '__main__':
    main()