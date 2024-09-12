list = [1,2,3,4,5]
print(list)

list.append(10)
print(f"List after append{list}")

list.insert(5,20)
print(f'list after add{list}')

list[5] = 143
print(f'list after updte{list}')

list.remove(1)
print(f'after remove{list}')

del list[2]
print(f'after delete second index {list}')

remove_last_element = list.pop()
print(f'after remove last element {remove_last_element}')

print("Access elemetn at index 2", {list[2]})


