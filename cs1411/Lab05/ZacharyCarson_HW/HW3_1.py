while(True):
    original_str = input("Enter a odd length sting: ")
    length = len(original_str)

    if(length%2 == 1):
        print("The middle character is: {}".format(original_str[int(length/2)]))
        print("The first half of the string is: {}".format(original_str[:int(length/2)]))
        print("The second half of the string is: {}".format(original_str[int(length/2)+1:]))
        break
    else:
        print("Plese try again.\n")
