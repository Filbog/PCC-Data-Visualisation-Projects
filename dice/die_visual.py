import plotly.express as px

from die import Die

die = Die()

# make and store some rolls
results = []
roll_num = 10000
for roll in range(roll_num):
    result = die.roll()
    results.append(result)

# analyze the results
frequencies = []
possible_results = range(1, die.num_sides + 1)
for val in possible_results:
    frequency = results.count(val)
    frequencies.append(frequency)

print(frequencies)
# visualise the results
title = f"Results of rolling D{die.num_sides} {roll_num} times"
labels = {"x": "Result", "y": "Frequency of result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.show()
