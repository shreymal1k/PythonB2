def display(list1)->None:
    total=0
    list2=[]
    for i in list1:
        total=total+i
        list2.append(total)
        
    length=len(list1)
    result = {
        "Sum": total,
        "Cumulative_sum": list2,
        "Average": total / length if length > 0 else 0,
        "Min": min(list1),
        "Max": max(list1)
    }
    return result

list1=[2,3,4,5,7,8,9]
val=display(list1)
print(val)