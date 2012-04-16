def next(x):
    original = x
    maximum = int("".join(sorted(list(str(x)), reverse=True)))

    while x < maximum:
        x += 1
        if sorted(list(str(x))) == sorted(list(str(original))):
            return x

    return -1

print 15432, next(15432)
print 4533, next(4533)
print 56456, next(56456)
print 154, next(154)
print 331, next(331)
