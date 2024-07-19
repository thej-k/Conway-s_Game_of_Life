import matplotlib.pyplot as plt


class GameOfLife(object):

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.x = x_dim
        self.y = y_dim
        self.life_grid = [[0 for _ in range(self.x)] for _ in range(self.y)]

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.life_grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        display_grid = self.get_grid()
        for i in range(self.y):
            for j in range(self.x):
                print(display_grid[i][j], '|', end=' ')
            print('\n- - - - - - - - - - - - - - - - - - - -')

    def populate_grid(self, coord):

        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for cd in coord:
            self.life_grid[cd[0]][cd[1]] = 1
        self.print_grid()

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
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
        # print(sum_grid)

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
        # Implement a method that applies the make_step method n times.
        for i in range(n):
            self.life_grid = self.make_step()

        return self.life_grid

    def draw_grid(self):
        # Draw the current state of the grid.
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


grid = GameOfLife(6, 6)
# grid_2 = grid.get_grid()
grid.print_grid()
print()
grid.populate_grid([(1, 1), (1, 3), (2, 1), (2, 3), (3, 2), (4, 2)])
grid.print_grid()
print()
grid.make_n_steps(3)
grid.print_grid()
grid.draw_grid()
