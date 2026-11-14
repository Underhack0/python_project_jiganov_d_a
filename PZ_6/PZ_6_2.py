def monot(A):
    if not A:
        return 0

    count = 1
    dir = 0

    for i in range(len(A) - 1):
        if A[i + 1] > A[i]:
            cdir = 1
        elif A[i + 1] < A[i]:
            cdir = -1
        else:
            continue

        if dir != 0 and dir != cdir:
            count += 1
        dir = cdir

    return count

print(monot([1,2,1]))
