import matplotlib.pyplot as plt


class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        """
        Initializes a new instance of the GameOfLife class with a grid of given dimensions.
        :param x_dim: The number of columns in the grid
        :param y_dim: The number of rows in the grid
        """

        self.x = x_dim
        self.y = y_dim
        self.life_grid = [[0 for _ in range(self.x)] for _ in range(self.y)]

    def get_grid(self):
        """
        gets the current state of the grid.
        :return:
        current state of the grid.
        """

        return self.life_grid

    def print_grid(self):
        """
        Print the grid in readable format
        """

        display_grid = self.get_grid()
        for i in range(self.y):
            for j in range(self.x):
                print(display_grid[i][j], '|', end=' ')
            print('\n')

    def populate_grid(self, coord):
        """
        Populates the game grid with live cells at specified coordinates
        :param coord:
        A list of tuples. Each tuple represents the (x,y) coordinates of a live cell.
        :return:
        The updated grid with live cells.
        """

        for cd in coord:
            self.life_grid[cd[0]][cd[1]] = 1
        self.print_grid()

    def make_step(self):
        """
        Update the grid by one step according to the rules of the Game of Life.
        :return:
        Updated grid
        """

        sum_grid = [[0 for _ in range(self.x)] for _ in range(self.y)]
        sum_of_live_cell = 0

        for i in range(self.y):
            for j in range(self.x):
                for a in range(i-1, i+2):
                    if not a < 0:
                        for b in range(j-1, j+2):
                            if not b < 0:
                                if not (a >= self.y or b >= self.x):
                                    if not (a == i and b == j):
                                        if self.life_grid[a][b] == 1:
                                            sum_of_live_cell += 1
                sum_grid[i][j] = sum_of_live_cell
                sum_of_live_cell = 0

        for i in range(self.y):
            for j in range(self.x):
                if self.life_grid[i][j] == 1:
                    if sum_grid[i][j] < 2:
                        self.life_grid[i][j] = 0
                    elif sum_grid[i][j] <= 3:
                        self.life_grid[i][j] = 1
                    else:
                        self.life_grid[i][j] = 0
                else:
                    if sum_grid[i][j] == 3:
                        self.life_grid[i][j] = 1

        return self.life_grid

    def make_n_steps(self, n):
        """
        Advance the game by specified number of steps
        :param n: Number of steps
        :return:
        Updated grid after n steps
        """

        for i in range(n):
            self.life_grid = self.make_step()

        return self.life_grid

    def draw_grid(self):
        """
        Visualizes the current state of the game grid using a scatter plot.
        :return:
        none
        """

        x = []
        y = []
        colors = []

        for rows in range(self.y):
            for cols in range(self.x):
                x.append(cols)
                y.append(rows)
                colors.append('yellow' if self.life_grid[rows][cols] == 1 else 'red')

        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(x, y, c=colors, s=100, edgecolors='k')

        ax.invert_yaxis()

        ax.set_xlim(-0.5, self.x - 0.5)
        ax.set_ylim(-0.5, self.y - 0.5)

        plt.title('Game of Life Grid')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()


# grid = GameOfLife(30, 30)
# grid.populate_grid([(14, 16), (15, 16), (16, 16), (18, 16), (19, 16), (20, 16),
# (16, 14), (16, 15), (16, 17), (16, 18),
# (18, 14), (18, 15), (18, 17), (18, 18),
# (14, 18), (15, 18), (16, 18), (18, 18), (19, 18), (20, 18)])
# grid.make_step()
# grid.make_n_steps(6)
# grid.draw_grid()
