#Step 1: Take an input string from the user
plaintext = input("Enter a string to encrypt: ")

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