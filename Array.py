#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

def size_memory(arr):
    print(arr)
    print(id(arr))
    for i in range(len(arr)):
        print("List Index --->", end=" ")
        print(i, ",", end=" ")
        print(" Value --->" ,arr[i], end=" ")
        print(", at Memory --->", end=" ")
        print(id(arr[i]))

stock_prices = [1,2,3,4,5]
size_memory(stock_prices)
stock_prices.insert(3,6)
size_memory(stock_prices)



# expenses = [['January', 2200],
#            ['February', 2350],
#            ['March', 2600],
#            ['April', 2130],
#            ['May', 2190]]

expenses = [('January', 2200),
            ('February', 2350),
            ('March', 2600),
            ('April', 2130),
            ('May', 2190)]

print('#1. In Feb, how many dollars you spent extra compare to January?')
print(expenses[1][1] - expenses[0][1])

print('#2.Find out your total expense in first quarter (first three months) of the year.')
total_expense = 0
for month, expense in expenses :
    if month in ('January','February','March'):
        total_expense += expense
print(total_expense)


te = 0
for i in range(len(expenses)):
    if i < 3:
        te += expenses[i][1]
print(te)

print('#3. Find out if you spent exactly 2000 dollars in any month')

for month, expense in expenses:
    if expense == 2000:
        print(month)
    else:
        print('1.No expense for 2000 in any month')


te = 0
for i in range(len(expenses)):
    if expenses[i][1] == 2000:
        print(expenses[i][0])
    else:
        print('2.No expense for 2000 in any month')

expenses.append(['June',1980])
print(len(expenses))

# 2.You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print('********************Problem second ******************************')
heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append('black panther')
print(heros)



heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
print(heros)


heros.sort()
print(heros)

heros = [x for x in heros if x not in ('thor','hulk')]
print(heros)
heros=['spider man','thor','hulk','iron man','captain america']
print(heros)
print(heros[1:3])
heros[1:3]=['doctor strange']
print(heros)

x = int(input("Enter a number less than 100 \n"))
print([i for i in range(1,x) if (i%2) != 0])
