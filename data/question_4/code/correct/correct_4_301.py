def sort_age(lst):
    if len(lst) == 1:
        return lst
    else:
        for j in range(len(lst) -1):
            for i in range(len(lst) -1):
                if lst[i][1] < lst[i+1][1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            
    return lst          

