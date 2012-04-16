
def sums_to(data, m):
    data.sort()
    while True:
        sum = data[0] + data[-1]
        if sum < m:
            data = data[1:]
        elif sum > m:
            data = data[:-1]
        else:
            print "Found", sum, "=", data[0], "+", data[-1]
            return True

        if len(data) <= 2: break

    return False

data = [1,2,3,5,7,10,19,23,30]

for i in range(50):
    sums_to(data, i)
