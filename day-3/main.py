import sys

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

# part 2
def calculate_co2_scrubbing_rating(binary_strings: list[str]) -> tuple[int, int, int]:
    def calculate_oxygen_rate(binary_strings: list[str]) -> int:
        binary_strings_copy = [x for x in binary_strings]
        for bit_position in range(len(binary_strings[0])):
            bit_counts = {"0":0, "1":0}

            for binary_string in binary_strings_copy:
                bit_counts[binary_string[bit_position]] += 1

            if (bit_counts["1"] > bit_counts["0"]):
                most_common_bit = '1'
            elif (bit_counts["1"] < bit_counts["0"]):
                most_common_bit = '0'
            else:
                most_common_bit = '1'

            binary_strings_copy = [x for x in binary_strings_copy if x[bit_position] == most_common_bit]

            if (len(binary_strings_copy) == 1):
                return int(binary_strings_copy[0], 2)

        return int(binary_strings_copy[0], base=2)

    def calculate_co2_rate(binary_strings: list[str]) -> int:
        binary_strings_copy = [x for x in binary_strings]
        for bit_position in range(len(binary_strings[0])):
            bit_counts = {"0":0, "1":0}

            for binary_string in binary_strings_copy:
                bit_counts[binary_string[bit_position]] += 1

            if (bit_counts["1"] > bit_counts["0"]):
                most_common_bit = '0'
            elif (bit_counts["1"] < bit_counts["0"]):
                most_common_bit = '1'
            else:
                most_common_bit = '0'

            binary_strings_copy = [x for x in binary_strings_copy if x[bit_position] == most_common_bit]

            if (len(binary_strings_copy) == 1):
                return int(binary_strings_copy[0], base=2)

        return int(binary_strings_copy[0], base=2)

    oxygen_rate = calculate_oxygen_rate(binary_strings)
    co2_rate = calculate_co2_rate(binary_strings)

    return (oxygen_rate, co2_rate, oxygen_rate * co2_rate)

if __name__ == "__main__":
    with open("day-3/input.txt", "r") as f:
        data = [x.strip() for x in f.readlines()]

    print("Gamma Rate: {}, Epsilon Rate: {}, Power Consumption Rate: {}".format(
        calculate_rates(data)[0],
        calculate_rates(data)[1], 
        calculate_rates(data)[2])
    )
    
    print("Oxygen Rate: {}, CO2 Rate: {}, CO2 Scrubbing Rate: {}".format(
        calculate_co2_scrubbing_rating(data)[0],
        calculate_co2_scrubbing_rating(data)[1],
        calculate_co2_scrubbing_rating(data)[2]
    ))