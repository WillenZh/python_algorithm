def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list[1:] if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

if __name__=="__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print qSort(a)
    