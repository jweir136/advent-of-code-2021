def count_increases(data: list[int]) -> int:
    num_increases = 0
    last_measurement = data[0]

    for i in range(1, len(data)):
        if (data[i] > last_measurement):
            num_increases += 1
        last_measurement = data[i]

    return num_increases

if __name__ == "__main__":
    with open("day-1/input.txt", "r") as f:
        data = [int(x) for x in f.read().split("\n")]

    print("Number of increases: {}".format(count_increases(data)))