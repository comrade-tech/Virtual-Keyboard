# importing the required module
import matplotlib.pyplot as plt


def graphh():
# x axis values
    x = [1, 2, 3, 4, 5, 6,11]
    # corresponding y axis values
    y = [2, 4, 1, 5, 2, 6,10]

    # plotting the points
    plt.plot(x, y, color='black', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # setting x and y axis range
    plt.ylim(1, 8)
    plt.xlim(1, 8)

    # naming the x axis
    plt.xlabel('frame fps')
    # naming the y axis
    plt.ylabel('letter')

    # giving a title to my graph
    plt.title('')

    # function to show the plot
    plt.show()


def graph1():
# x axis values
    x = [2, 5, 6, 7, 8, 10,11]
    # corresponding y axis values
    y = [2, 7, 6, 8, 9,10,11]

    # plotting the points
    plt.plot(x, y, color='black', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # setting x and y axis range
    plt.ylim(1, 8)
    plt.xlim(1, 8)

    # naming the x axis
    plt.xlabel('frame fps')
    # naming the y axis
    plt.ylabel('letter')

    # giving a title to my graph
    plt.title('')

    # function to show the plot
    plt.show()


def graph2():
# x axis values
    x = [10, 12, 13, 14, 15, 16]
    # corresponding y axis values
    y = [11, 13, 14, 15, 15, 16]

    # plotting the points
    plt.plot(x, y, color='black', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # setting x and y axis range
    plt.ylim(1, 8)
    plt.xlim(1, 8)

    # naming the x axis
    plt.xlabel('frame fps')
    # naming the y axis
    plt.ylabel('letter')

    # giving a title to my graph
    plt.title('')

    # function to show the plot
    plt.show()


def graph3():
# x axis values
    x = [2, 5, 6, 7, 8, 10,11]
    # corresponding y axis values
    y = [2, 7, 6, 7, 8,10,12]

    # plotting the points
    plt.plot(x, y, color='black', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

    # setting x and y axis range
    plt.ylim(1, 8)
    plt.xlim(1, 8)

    # naming the x axis
    plt.xlabel('frame fps')
    # naming the y axis
    plt.ylabel('letter')

    # giving a title to my graph
    plt.title('')

    # function to show the plot
    plt.show()