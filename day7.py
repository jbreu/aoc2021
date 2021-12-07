import statistics

with open('input7') as f:
    crabs = [line.rstrip().split(",") for line in f][0]
    crabs = [int(c) for c in crabs]

low = statistics.median_low(crabs)
high = statistics.median_high(crabs)

# 1st task

low_diff = sum(abs(c - low) for c in crabs)
high_diff = sum(abs(c - high) for c in crabs)

print(min(low_diff, high_diff))

# 2nd task


def gauss_sum(num):
    return int((num * num + num) / 2)


low_diff = sum(gauss_sum(abs(c - low)) for c in crabs)
high_diff = sum(gauss_sum(abs(c - high)) for c in crabs)

print(min(low_diff, high_diff))
