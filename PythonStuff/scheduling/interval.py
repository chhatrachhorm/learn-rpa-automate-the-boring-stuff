import time

print(time.time())


def calc_prod():
    product = 1
    for i in range(1, 10000):
        product = product * i
    return product


start = time.time()
prod = calc_prod()
end = time.time()
print('Took %s seconds to run' % (end - start))
print('Rounding', str(round(end - start, 2)))
