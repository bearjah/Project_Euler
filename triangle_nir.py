def read(fil):
    triangles = []
    with open(fil, 'r') as source:
        for line in source:
            parse = line.rstrip().split(',')
            print(parse)
            cur = []
            for i in range(0, 6, 2):
                cur.append((int(parse[i]), int(parse[i + 1])))
            triangles.append(cur)
    print(triangles)
    return triangles


def area(A, B, C):
    S = 0.5 * abs((A[0] - C[0])(B[1] - A[1]) - (A[0] - B[0])(C[1] - A[1]))

    return S


def work(fil):
    triangles = read(fil)
    count = 0
    for A, B, C in triangles:
        total = area(A, B, C)
        part1 = area(A, B, (0, 0))
        part2 = area(A, C, (0, 0))
        part3 = area(B, C, (0, 0))
        if (part1 > 0) and (part2 > 0) and (part3 > 0) and (part1 + part2 + part3 == total):
            count += 1

    return count


if __name__ == '__main__':
    count = work('p102_triangles.txt')