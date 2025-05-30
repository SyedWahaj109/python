## if else ##
age = int(input("Enter your age"))

if age >= 18:
    print("you can vote")
else:
    print("you cant vote")
## if else ##

## for loop ##
for i in range(1,20,1):
    print(i)
## for loop ##

## while loop ##
a = 0
while a < 11:
    print(a)
    a = a + 1
## while loop ##

## for Break ##
for b in range(1, 21):
    print(b)
    if b == 10:
        break
## for Break ##

## while Break ##
c = 0
while c < 21:
    print(c)
    c = c + 1
    if c == 10:
        break
## while Break ##

## for continue  ##
for d in range(1,5):
    if d == 2:
        continue
    print(d)
## for continue  ##