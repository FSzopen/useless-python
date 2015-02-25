import random

pinit = 0
p = pinit
alphainit = 0.001
res = dict(dict())

for i in range(100):
    buff = ""
    p = p + 0.01
    alpha = alphainit
    for j in range(100):
        alpha = alpha + 0.001
        l = []
        for n in range(5000):
            count = 0
            u = 0
            while u < (p - alpha):
                count += 1
                x = random.randrange(0, 1000)/1000.
                if x < p:
                    u = (1-alpha)*u + alpha
                else:
                    u = (1-alpha)*u
            l.append(count)
        if buff:
            buff += ";" + str(reduce(lambda x, y: x + y, l)/len(l))
        else:
            buff += str(reduce(lambda x, y: x + y, l)/len(l))
    print buff
