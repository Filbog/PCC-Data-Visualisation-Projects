import plotly.express as px
import matplotlib.pyplot as plt
from die import Die

# create two D6 dice


die_1 = Die()
die_2 = Die()

# make some rolls
results = []
roll_num = 100000
for roll in range(roll_num):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result + 1)
for val in possible_results:
    frequency = results.count(val)
    frequencies.append(frequency)

# visualize the results
title = (
    f"Results of rolling a D{die_1.num_sides} and a D{die_2.num_sides} {roll_num} times"
)
labels = {"x": "Result", "y": "Frequency of result"}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
# fig.write_html("dice_visual_d6d10.html")
fig.show()

# visualize the results
fig, ax = plt.subplots()
ax.bar(possible_results, frequencies)
plt.xticks(possible_results)
ax.set_title("Results of rolling two D6 dice")
ax.set_xlabel("Result")
ax.set_ylabel("Frequency of Result")

plt.show()
