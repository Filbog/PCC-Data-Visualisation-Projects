import matplotlib.pyplot as plt


def nums_and_their_cubes(range_end):
    """Return a list of numbers and their cubes."""
    nums = [num for num in range(1, range_end + 1)]
    cubes = [num**3 for num in nums]
    return nums, cubes


def plot_cubes(nums, cubes, annotate=False):
    """Plot the numbers and their cubes."""
    fig, ax = plt.subplots()
    ax.plot(nums, cubes, linewidth=1)
    ax.scatter(nums, cubes, c=cubes, cmap=plt.cm.magma, s=10)

    # Add annotations for each point
    if annotate == True:
        for num, cube in zip(nums, cubes):
            ax.annotate(
                str(cube), (num, cube), textcoords="offset points", xytext=(-5, 10)
            )

    ax.set_title("Cubes", fontsize=20)
    ax.set_xlabel("Value", fontsize=12)
    ax.set_ylabel("Cube of Value", fontsize=12)
    ax.ticklabel_format(style="plain")
    ax.tick_params(axis="both", labelsize=10)
    plt.show()


# nums, cubes = nums_and_their_cubes(5)
nums, cubes = nums_and_their_cubes(5000)
# print(nums)
# print(cubes)
print(5000**3)
plot_cubes(nums, cubes)
