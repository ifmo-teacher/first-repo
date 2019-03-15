import time
t = True
x = 0
while t:
    print('test')
    time.sleep(1)
    x += 1
    if x == 10:
        t = False
