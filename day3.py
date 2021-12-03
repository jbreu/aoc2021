from day3_helpers import get_most_common_bit, binlisttoint, invert_binary_list

# Fifth task

with open('input3') as f:
    lines3_in = [list(map(int, line.rstrip())) for line in f]

gamma_bin = get_most_common_bit(lines3_in)
gamma_num = binlisttoint(gamma_bin)

epsilon_bin = invert_binary_list(gamma_bin)
epsilon_num = binlisttoint(epsilon_bin)

print(gamma_num * epsilon_num)

# Sixth task

oxygen = lines3_in
co2scrubber = lines3_in

for i in range(len(oxygen[0])):
    if len(oxygen) > 1:
        oxygen = [a for a in oxygen if a[i] == get_most_common_bit(oxygen, i)]
    if len(co2scrubber) > 1:
        co2scrubber = [a for a in co2scrubber if a[i] != get_most_common_bit(co2scrubber, i)]

print(binlisttoint(oxygen[0]) * binlisttoint(co2scrubber[0]))
