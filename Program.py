import pyautogui
import time

# Define the grid coordinates
left_upper_corner = (533, 153)
right_lower_corner = (1513, 686)

repetitions = 30
start_x, start_y = 533,153
end_x, end_y = 1513,686
step = 69
# Calculate the step size for the grid


# Delay before starting to give you time to focus on the target area
time.sleep(3)
pyautogui.PAUSE = 0.0
pyautogui.MINIMUM_DURATION = 0.0
# Click in a grid-like pattern
for repetition in range(repetitions):
    for y in range(start_y, end_y+1, step):
        for x in range(start_x, end_x+1, step):

            pyautogui.click(x, y)
            #time.sleep(0.5)  # Adjust the delay as needed



# Done
print("Grid clicks completed.")
