import os
import time

num = int(input("m,n up to ... "))

know_lst = [[0,0], [0,1], [1,0], [0,2], [1,1], [2,0]] # points we know at first
# we know that ∫sin^m x cos x dx = (sin^m+1 x)/m+1 + c
# we know that ∫sin x cos^n x dx = -(cos^n+1 x)/n+1 + c
for m in range(2, 2*num): know_lst.append([m, 1])
for n in range(2, 2*num): know_lst.append([1, n])
display_lst = []

def display():  
    for y in range(num, -1, -1):
        print(y % 10, end="", flush=True)
        for x in range(0, num + 1):
            if [x, y] in display_lst:
                print("   o", end="", flush=True)
            else:
                print("    ", end="", flush=True)
        print("\n")
    axis = " "
    for i in range(num + 1): axis += "   " + str(i % 10)
    print(axis, "\n")

# we know that ∫sin^m x cos^m x dx = ∫sin^m (2x) dx / 2^m => let this be formula 1
def formula1(x):
    if [x,0] in know_lst:
        if [x,x] not in know_lst: know_lst.append([x,x])

# we know that ∫sin^m x cos^n x dx = ∫sin^m x cos^n-2 x dx - ∫sin^m+2 x cos^n-2 x dx => let this be formula 2
def formula2(x,y):
    if [x,y] and [x+2,y] in know_lst:
        if [x,y+2] not in know_lst: know_lst.append([x,y+2])
    if [x,y] and [x,y+2] in know_lst:
        if [x+2,y] not in know_lst: know_lst.append([x+2,y])

# we know sin and cos are complementary so replacing x with π/2 - x can swap m and n
def formula3(x,y):
    if [x,y] in know_lst:
        if [y,x] not in know_lst: know_lst.append([y,x])


change = True
while change:
    start = len([[x,y] for [x,y] in know_lst if x <= num and y <= num]) # display list at the beginning
    change1 = True
    change2 = True
    change3 = True

    for [m,n] in [[x,y] for [x,y] in know_lst if y == 0]:
        formula1(m)
    if len([[x,y] for [x,y] in know_lst if x <= num and y <= num]) > start: # display list increases
        start = len([[x,y] for [x,y] in know_lst if x <= num and y <= num])
    else: change1 = False

    for [m,n] in know_lst:
        formula2(m, n)
    if len([[x,y] for [x,y] in know_lst if x <= num and y <= num]) > start: # display list increases
        start = len([[x,y] for [x,y] in know_lst if x <= num and y <= num])
    else: change2 = False

    for [m,n] in know_lst:
        formula3(m,n)
    if len([[x,y] for [x,y] in know_lst if x <= num and y <= num]) > start: # display list increases
        pass
    else: change3 = False

    if change1 == change2 == change3 == False: change = False

# set up
for point in range(len(know_lst) - 1, -1, -1):
    if know_lst[point][0] <= num and know_lst[point][1] <= num and know_lst.count(know_lst[point]) == 1:
        pass
    else:
        know_lst.pop(point)

# animation
def animate(start, end):
    for i in range(start, end):
        display_lst.append(know_lst[i])
        os.system("clear")
        display()
        time.sleep(0.1)
animate(0, 6)
stop = input()
animate(6, len(know_lst))

# unknown list
print("m, n we dont know ->")
for x in range(0, num + 1):
    for y in range(0, num + 1):
        if [x,y] not in display_lst:
            print(x, ",", y)
