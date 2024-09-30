def modify_immutable(x):
    x+=1
    print(f"Inside Function :{x}")
a=5
modify_immutable(a)
print(f"Outside Function:{a}")# Output : 5 (Unchanged)



def modify_mutable(lst):
    lst.append(4)
    print(f"Insdie fucntion:{lst}")

my_list=[1,2,3]
modify_mutable(my_list)
print(f"Outside fucntion:{my_list}")
