
def coin_sum(val):
    possible_values = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    poss_sum = 0
    for i1 in range(val, 0, -possible_values[7]):
        for i2 in range(i1, 0, -possible_values[6]):
            for i3 in range(i2, 0, -possible_values[5]):
                for i4 in range(i3, 0, -possible_values[4]):
                    for i5 in range(i4, 0, -possible_values[3]):
                        for i6 in range(i5, 0, -possible_values[2]):
                            for i7 in range(i6, 0, -possible_values[1]):
                                # for i8 in range(i7, int(val / possible_values[0])):
                                # print(i1, i2, i3, i4, i5, i6, i7, i8)
                                poss_sum += 1
    return poss_sum


def coin_sum_dp(val):
    possible_values = np.array([1, 2, 5, 10, 20, 50, 100, 200])
    ways = np.zeros(val+1)
    ways[0] = 1
    for i in range(len(possible_values)):
        for j in range(possible_values[i], val+1):
            ways[j] += ways[j - possible_values[i]]
    return ways[val]


if __name__ == '__main__':
    # print('coin sum ways count:', coin_sum_dp(200))
