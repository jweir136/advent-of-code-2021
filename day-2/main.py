import sys

position_x = 0
position_y = 0
aim = 0

# part 1
def move_position(direction: str, units: int) -> None:
    global position_x
    global position_y

    if (direction == "forward"):
        position_x += units
    elif (direction == "down"):
        position_y += units
    elif (direction == "up"):
        position_y -= units

# part 2
def move_position_manual(direction: str, units: int) -> None:
    global position_x
    global position_y
    global aim

    if (direction == "down"):
        aim += units
    elif (direction == "up"):
        aim -= units
    elif (direction == "forward"):
        position_x += units
        position_y += (aim * units)

if __name__ == "__main__":
    with open("day-2/input.txt", "r") as f:
        for line in f.readlines():
            direction = line.split(" ")[0]
            units = int(line.split(" ")[1])

            if (int(sys.argv[1]) == 1):
                move_position(direction, units)
            elif (int(sys.argv[1]) == 2):
                move_position_manual(direction, units)

    print("X: {}, Y: {}, Total: {}".format(position_x, position_y, position_x * position_y))