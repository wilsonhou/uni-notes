def remove_quotes(ls):
    # make copy of list
    new_list = []
    # iterate through the list!
    i = 0
    while i < len(ls):
        # add elements to the new list
        new_list.append(int(ls[i]))
        i += 1
    # return the new list!
    return new_list


print(remove_quotes(['1', '2', '3']))
