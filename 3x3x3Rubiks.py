import numpy as np
import trimesh

# Define the size of the Rubik's cube
cube_size = 3
small_cube_size = 1.0
gap = 0.1

# Create a list to store all small cubes
cubes = []

# Iterate through all positions in the 3x3x3 Rubik's cube
for x in range(cube_size):
    for y in range(cube_size):
        for z in range(cube_size):
            # Create a small cube and translate it to the correct position
            cube = trimesh.creation.box(extents=[small_cube_size, small_cube_size, small_cube_size])
            cube.apply_translation([
                x * (small_cube_size + gap),
                y * (small_cube_size + gap),
                z * (small_cube_size + gap)
            ])
            cubes.append(cube)

# Combine all small cubes into one mesh
rubiks_cube = trimesh.util.concatenate(cubes)

# Export the Rubik's cube to an STL file
rubiks_cube.export('/mnt/c/Users/Ralph/rubiks_cube.stl')
