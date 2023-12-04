import plotly.express as px
from die import Die

# create multiple D6 dice

die_num = 2
dice = [Die() for _ in range(die_num)]

# make some rolls
results = []
roll_num = 1000
for roll in range(roll_num):
    result = sum([die.roll() for die in dice])
    results.append(result)

# analyze the results
frequencies = []
max_result = die_num * dice[0].num_sides
possible_results = range(die_num, max_result + 1)
for val in possible_results:
    frequency = results.count(val)
    frequencies.append(frequency)

# visualize the results
title = f"Results of rolling {die_num} D6 {roll_num} times"
labels = {"x": "Result", "y": "Frequency of result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html("dice_visual_d6d10.html")
fig.show()
