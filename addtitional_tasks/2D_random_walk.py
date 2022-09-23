# 2D random walk. A two-dimensional random walk simulates the behavior of a particle moving in a grid of points.
# At each step, the random walker moves north, south, east, or west with probability equal to 1/4,
# independent of previous moves. Write a program that takes an integer command-line argument n
# and estimates how long it will take a random walker to hit the boundary
# of a 2n-by-2n square centered at the starting point

import random
from time import time, sleep

n = int(input("Please select an integer: "))

table = [[' ' for i in range(2*n+1)] for j in range(2*n+1)]

particle = table[n][n]              # initial coordinates, in the center
particle_x, particle_y = n, n

start_time = time()
while particle_x not in [0, 2*n] and particle_y not in [0, 2*n]:
    table[particle_x][particle_y] = '💫'     # helps us to track the particle :)
    # move_direction = random.choice([particle_x-1, particle_x+1, particle_y-1, particle_y+1])
    move_direction = random.choice(['x', 'y'])
    if move_direction == 'x':
        particle_x = random.choice([particle_x-1, particle_x+1])
    else:
        particle_y = random.choice([particle_y-1, particle_y+1])
    print((particle_x, particle_y))

    table[particle_x][particle_y] = '🌠'     # represent the visual particle
    for row in table:
        print(row)
    sleep(1)        # increases a lot the time of execution but looks really nice

print("The random walker had run for ", time()-start_time)

