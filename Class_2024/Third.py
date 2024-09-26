# final code 

def display(list1)->None:
    total=0
    list2=[]
    for i in list1:
        total=total+i
        list2.append(total)
        
    length=len(list1)
    result = {
        'sum': total,
        'cumulative_sum': list2,
        'average': total / length if length > 0 else 0,
        'min': min(list1),
        'max': max(list1)
    }
    return result


def input_from_user_element():
    n=int(input("Enter the number :"))
    list1=[]
    for i in range(0,n):
        user=int(input(f"Enter the element {i}:"))
        list1.append(user)
    val=display(list1)
    print(val)
    
input_from_user_element()