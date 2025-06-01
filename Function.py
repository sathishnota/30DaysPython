def sum_avg(list_1):
    total = sum(list_1)
    avg = total/len(list_1)
    return total,avg


list1 = [56,87,96,35,87,12]

total,avg = sum_avg(list1)
print(total)
print(avg)


