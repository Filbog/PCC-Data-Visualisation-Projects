import plotly.graph_objects as go
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(500)
    rw.fill_walk()

    p_fig = go.Figure(
        data=go.Scatter(x=rw.x_values, y=rw.y_values, mode="lines+markers")
    )
    p_fig.show()

    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    print(point_numbers)
    # ax.scatter(
    #     rw.x_values,
    #     rw.y_values,
    #     c=point_numbers,
    #     cmap=plt.cm.Blues,
    #     edgecolors="none",
    #     s=5,
    # )
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.set_aspect("equal")
    # emphasize first and last points
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Another walk? (y/n)")
    if keep_running == "n":
        break
