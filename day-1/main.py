# part 1
def count_increases(data: list[int]) -> int:
    num_increases = 0
    last_measurement = data[0]

    for i in range(1, len(data)):
        if (data[i] > last_measurement):
            num_increases += 1
        last_measurement = data[i]

    return num_increases

# part 2
def count_increases_sliding_window(data: list[int]) -> int:
    num_increases = 0
    last_sum = data[0] + data[1] + data[2]

    for i in range(1, len(data)):
        if (sum(data[i:i+3]) > last_sum):
            num_increases += 1
        last_sum = sum(data[i:i+3])

    return num_increases

if __name__ == "__main__":
    with open("day-1/input.txt", "r") as f:
        data = [int(x) for x in f.read().split("\n")]

    print("Number of increases: {}".format(count_increases(data)))
    print("Number of increases w/ sliding window: {}".format(count_increases_sliding_window(data)))