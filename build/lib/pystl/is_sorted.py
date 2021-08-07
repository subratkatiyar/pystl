def is_sorted(list1):
    flag = 0
    list2 = list1[:]
    list1.sort()
    if (list1 == list2):
        flag = 1
    if (flag) :
        return True
    else :
        return False