from tools import get_input_list

test = False
ranges, _ = get_input_list(test)


def parse_ranges(ranges_str):
    intervals = []
    for ch in ranges_str:
        start_str, end_str = ch.split("-")
        start, end = int(start_str), int(end_str)
        intervals.append((start, end))
    return intervals


def total_covered_length(intervals: list[tuple[int, int]]):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[0])

    total = 0
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start > cur_end + 1:
            total += cur_end - cur_start + 1
            cur_start, cur_end = start, end
        else:
            cur_end = max(cur_end, end)
    total += cur_end - cur_start + 1
    return total


def main():
    intervals = parse_ranges(ranges)
    count_fresh = total_covered_length(intervals)
    print(count_fresh)


main()
