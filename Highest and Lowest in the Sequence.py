# Track the highest and lowest weight entered.
highest_weight = 0
lowest_weight = 0

for analysis in range(1, 6):
    weight = float(input('Weight of the {}th person: '.format(analysis)))
    if analysis == 1:
        highest_weight = weight
        lowest_weight = weight
    else:
        if weight > highest_weight:
            highest_weight = weight
        if weight < lowest_weight:
            lowest_weight = weight

# Display the final result.
print('The highest recorded weight was {}Kg'.format(highest_weight))
print('The lowest recorded weight was {}Kg'.format(lowest_weight))