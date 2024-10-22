import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ROWS = 30
COLS = 50
ON = 255
OFF = 0

grid = np.full((ROWS, COLS), OFF)

print("Enter coordinates (row, col) for cells to be ON. Type 'done' when finished")
while True:
    user_input = input("Enter row and column (example, 10 20): ")
    if user_input.lower() == "done":
        break
    try:
        row, col = map(int, user_input.split())
        if 0 <= row < ROWS and 0 <= col < COLS:
            grid[row, col] = ON
        else:
            print(f"Invalid input. Please enter row values between 0 and 29 and column values between 0 and 49.")
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space, or 'done'.")

def update(data):
    global grid
    newGrid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            # checking the rows/columns around with toroidal boundary conditions for wrapping around the grid
            total = (grid[i, (j-1)%COLS] + grid[i, (j+1)%COLS] +
                     grid[(i-1)%ROWS, j] + grid[(i+1)%ROWS, j] +
                     grid[(i-1)%ROWS, (j-1)%COLS] + grid[(i-1)%ROWS, (j+1)%COLS] +
                     grid[(i+1)%ROWS, (j-1)%COLS] + grid[(i+1)%ROWS, (j+1)%COLS]) / 255
            # 255 is the normalization number
            # Conway's rules
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON
    # the grid data
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]

# the animation
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='gray')
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
plt.show()
