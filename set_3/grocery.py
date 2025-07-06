#Functions
def count_list(array):
    show_item = []

    x = 0
    y = 0

    #Count repeat items
    while x != len(array):
        count = 0
        k = x
        while y != len(array):
            if array[x] == array [y]:
                count = count + 1
                y = y+ 1
            else:
                break
        x = y
        #Show number and items
        count_str = str(count)
        show_item.append(count_str +" "+ array[k])

    return show_item

def show_list(array):
    for i in range(len(array)):
        print(array[i])

#Add list
items = []
final_items = []
while True:
    try:
        component = input("")

        items.append(component.upper())

    except EOFError:
        break

print("\n")
#sorted list
items.sort()

final_items = count_list(items)

show_list(final_items)