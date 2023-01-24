# Open both files and put them into the list. For the sake of consistency, lists are sorted
f = open('Old List.txt', 'r', errors='ignore')
list1 = []
for x in f:
    list1.append(x)
f.close


# All list items end with \n so we'll remove that
for x in range(len(list1)-1):
    list1[x] = list1[x][0:-1]

f = open('New List.txt', 'r', errors='ignore')
list2 = []
for x in f:
    list2.append(x)
f.close


# All list items end with \n so we'll remove that
for x in range(len(list2)-1):
    list2[x] = list2[x][0:-1]
# Lists are sorted for consistency
list1.sort()
list2.sort()
list3 = []
debug = []
# Print statements included after every action for debug purposes. 
print('Full lists of old items:\n\n'+str(list1)+'\n\n')
debug.append(('Full lists of old items:\n\n'+str(list1)+'\n\n'))
print('Full list of new items:\n\n'+str(list2)+ '\n')
debug.append(('Full list of new items:\n\n'+str(list2)+ '\n'))
# Make a list which doesn't include any numbers
# Since all items separate name and number by a semicolon, that is used as a breakpoint.
# All things before the semicolon are selected to get the name, all things after the semicolon to get number
def getname(name):
    list = []
    for x in name:   
        place = x.find(':')+2
        list.append(x[:place])
    return list
# Make a list which doesn't include any letters.
def getnum(num):
    list = []
    for x in num:
        place = x.find(':')
        temp = x[place+1:]
        temp2 = temp.strip()
        list.append(int(temp2))
    return list
# Create numberless lists for comparisons
name1 = getname(list1)
name2 = getname(list2)
print('Full list of numberless old items:\n\n'+str(name1)+'\n\n')
debug.append(('Full list of numberless old items:\n\n'+str(name1)+'\n\n'))
print('Full list of numberless old items:\n\n'+str(name1)+'\n\n')
debug.append(('Full list of numberless new items:\n\n'+str(name2)+'\n\n'))
counter = 0
new = []
more = []

# Lists are compared against eachother.
# When an item appears in the new list but not the old, it is placed into new
# When an item appears in the new list and the old, it is placed into more.

for x in name2:
    if x not in name1:
        new.append(list2[counter])
    else:
        more.append(list2[counter])
    counter += 1
print('Things that are completely new:\n\n'+str(new)+'\n\n')
debug.append(('Full list of numberless old items:\n\n'+str(name1)+'\n\n'))

# If an item is new, it goes directly into the final list which is then sorted

list3 = list3+new
list3.sort()

#Without numbers the program can't distinguish if you have placed more of an item or if all of said item was already placed
#By comparing more against the list of old items, you can weed out items which have unchanged numbers they are thrown out

temp = []
for x in more:
    if x not in list1:
        temp.append(x)
print('Items that are already placed which need additional of the same items placed:\n\n'+str(temp)+'\n\n')
debug.append(('Items that are already placed which need additional of the same items placed:\n\n'+str(temp)+'\n\n'))
more = temp
morestrip = getname(more)
counter = 0
comp = []

# Fetch items from the old list which have changed values in the new list

for x in name1:
    if x in morestrip:
        comp.append(list1[counter])
    counter += 1
print('Items and corresponding values from the old list:\n\n'+str(comp)+'\n\n')
debug.append(('Items and corresponding values from the old list:\n\n'+str(comp)+'\n\n'))
# Fetch only the numbers from both lists so math can be done

morenum = getnum(more)
print('Amounts of items from the new list:\n\n'+str(morenum)+'\n\n')
debug.append(('Amounts of items from the new list:\n\n'+str(morenum)+'\n\n'))
compnum = getnum(comp)
print('Amounts of Items from the old list:\n\n'+str(compnum)+'\n\n')
debug.append(('Amounts of Items from the old list:\n\n'+str(compnum)+'\n\n'))

# Math is performed. New list will have more items, so the old values are subtracted from the new, giving us the difference

ziplist = zip(morenum, compnum)
sum = [x-y for (x,y) in ziplist]
print(sum)
temp = []
for x in sum:
    temp.append(str(x))
sum = temp
print('Difference in the numbers between new and old items:\n\n'+str(sum)+'\n\n')
debug.append(('Difference in the numbers between new and old items:\n\n'+str(sum)+'\n\n'))
final = []

# Finallly the list of items are fixed and their corrected values placed on the correct items

counter = 0
for x in morestrip:
    final.append(x+sum[counter])
    counter += 1
list3 = list3+final
list3.sort()

# Finally \n is placed at the end of each string, making line breaks after each item

for x in range(len(list3)-1):
    list3[x] = f"{list3[x]}\n"
print('Full list of items to be purchased:\n\n'+str(list3)+'\n\n')
debug.append(('Full list of items to be purchased:\n\n'+str(list3)+'\n\n'))

# Write to file

f = open('Purchase List.txt', 'w', errors='ignore')
for x in list3:
    f.write(x)
f.close()

f = open('debug.txt', 'w', errors='ignore')
for x in debug:
    f.write(x)
f.close()
