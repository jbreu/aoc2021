with open('input6') as f:
    fish = [line.rstrip().split(",") for line in f][0]
    fish = [int(num) for num in fish]

fish_ages = {i: 0 for i in range(9)}

for f in fish:
    fish_ages[f] += 1

for _ in range(1, 257):
    old_fish_ages = dict(fish_ages)

    fish_ages[8] = old_fish_ages[0]
    fish_ages[7] = old_fish_ages[8]
    fish_ages[6] = old_fish_ages[7] + old_fish_ages[0]
    fish_ages[5] = old_fish_ages[6]
    fish_ages[4] = old_fish_ages[5]
    fish_ages[3] = old_fish_ages[4]
    fish_ages[2] = old_fish_ages[3]
    fish_ages[1] = old_fish_ages[2]
    fish_ages[0] = old_fish_ages[1]

print(sum(v for k, v in fish_ages.items()))
