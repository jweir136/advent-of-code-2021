# part 1
def calculate_rates(binary_strings: list[str]) -> tuple[int,int,int]:
    gamma_rate = ""
    epsilon_rate = ""

    for bit_position in range(len(binary_strings[0])):
        bit_counts = {"0":0, "1":1}

        for binary_string in binary_strings:
            bit_counts[binary_string[bit_position]] += 1

        if (bit_counts["1"] > bit_counts["0"]):
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return (int(gamma_rate, base=2), int(epsilon_rate, base=2), int(gamma_rate, base=2)*int(epsilon_rate, base=2))

if __name__ == "__main__":
    with open("day-3/input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    print("Gamma Rate: {}, Epsilon Rate: {}, Power Consumption Rate: {}".format(
        calculate_rates(data)[0],
        calculate_rates(data)[1], 
        calculate_rates(data)[2])
    )