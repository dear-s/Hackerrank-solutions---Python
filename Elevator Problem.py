def solution(elevator_starts, elevator_heights, target_floor):

    # elevetors to take minimize it
    start_end = {}

    for i in range(len(elevator_starts)):
        if elevator_starts[i] not in start_end:
            start_end[elevator_starts[i]] = [elevator_heights[i] + elevator_starts[i]]
        else:
            start_end[elevator_starts[i]].append(elevator_heights[i] + elevator_starts[i])

    print("start_end: ", start_end)

    begin = 0 # start from ground floor
    end = target_floor
    arrays = []
    rec(start_end, begin, end, arrays, [])

    print("arrays: ", arrays)

    get_lengths = []

    for a in arrays:
        get_lengths.append(len(a))

    if len(get_lengths) == 0:
        return -1

    return min(get_lengths)-1


def rec(start_end, begin, end, arrays, path):

    if begin == end:
        arrays.append(path + [begin])
        return

    if begin in start_end:
        end_vals = start_end[begin]
        for e in end_vals:
            if e > begin:
                for i in range(begin+1, e+1):
                    if begin in path:
                        return
                    else:
                        rec(start_end, i, end, arrays, path + [begin])
            else:
                for i in range(begin-1, e-1, -1):
                    if begin in path:
                        return
                    else:
                        rec(start_end, i, end, arrays, path + [begin])

    else:
        return


elevator_starts = [0,10,1,4,2,5,3,5,1]
elevator_heights = [1,-2,1,2,3,5,6,2,4]
target_floor = 5
ans = solution(elevator_starts, elevator_heights, target_floor)

print("Answer: ", ans)
