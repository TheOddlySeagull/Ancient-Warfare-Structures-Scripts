# This script will generate AW structure town wall blueprint strings.

import os
import sys

# Set the size of the wall to generate:
wall_size_start_s = sys.argv[1]
wall_size_end_s = sys.argv[2]
wall_size_start_i = int(wall_size_start_s)
wall_size_end_i = int(wall_size_end_s)


# Set the number of elements between 2 towers:
wall_tower_spacing_i = int(sys.argv[3])
wall_tower_spacing_s = str(wall_tower_spacing_i)

# Set if we don't care, or want 2 towers or walls at the gate:
wall_gate_towers_odd = 1
wall_gate_towers_even = 1
#0: walls on each side of the gate
#1: towers on each side of the gate
#2: we don't care

# Set the wall element ids:
wall_angle_id = '0'
wall_straight_id = '1'
wall_gate_odd_id = '2'
wall_gate_even_left_id = '3'
wall_gate_even_right_id = '4'
wall_tower_id = '5'

print("Generating walls from size " + wall_size_start_s + " to " + wall_size_end_s + ", with " + wall_tower_spacing_s + " straight walls between 2 towers.")

#We create or clean a file called "generated_walls.txt" to store the generated walls:
f = open("generated_walls.txt", "w")
f.write("wallPatterns:\n")

##############################################################################################################
# We check if parameters are correct:
##############################################################################################################

if wall_size_start_i < 5:
    print("Error: minimum (" + wall_size_start_s + ") must at least be 5.")
    sys.exit(1)
if wall_size_end_i < wall_size_start_i:
    print("Error: maximum (" + wall_size_end_s + ") must be greater than minimum (" + wall_size_start_s + ").")
    sys.exit(1)
if wall_tower_spacing_i < 0:
    print("Error: tower spacing (" + wall_tower_spacing_s + ") must be greater than 0.")
    sys.exit(1)

##############################################################################################################
# We generate the gate segments:
##############################################################################################################

# Odd gate:
if wall_gate_towers_odd == 1:
    # We generate the gate with towers:
    generated_gate_odd = wall_tower_id + '-' + wall_gate_odd_id + '-' + wall_tower_id
    gate_segment_size_odd = 3
else:
    if wall_gate_towers_odd == 0:
        # We generate the gate with walls:
        generated_gate_odd = wall_straight_id + '-' + wall_gate_odd_id + '-' + wall_straight_id
        gate_segment_size_odd = 3
    else:
        # We generate the gate:
        generated_gate_odd = wall_gate_odd_id
        gate_segment_size_odd = 1

# Even gate:
if wall_gate_towers_even == 1:
    # We generate the gate with towers:
    generated_gate_even = wall_tower_id + '-' + wall_gate_even_left_id + '-' + wall_gate_even_right_id + '-' + wall_tower_id
    gate_segment_size_even = 4
else:
    if wall_gate_towers_even == 0:
        # We generate the gate with walls:
        generated_gate_even = wall_straight_id + '-' + wall_gate_even_left_id + '-' + wall_gate_even_right_id + '-' + wall_straight_id
        gate_segment_size_even = 4
    else:
        # We generate the gate:
        generated_gate_even = wall_gate_even_left_id + '-' + wall_gate_even_right_id
        gate_segment_size_even = 2

##############################################################################################################
# We generate the walls:
##############################################################################################################

for wall_size in range(wall_size_start_i, wall_size_end_i + 1):
    # We generate the empty wall and reset the counters:
    generated_wall = ''
    half_wall_element_count_processed = 0
    wall_tower_spacing_current = 0

    #########################################################################
    # We calculate the number of elements on each side of the gate:
    #########################################################################

    #Test if odd or even:
    if (wall_size % 2) == 0:
        wall_is_even = 1
        half_wall_element_count_total = (wall_size - gate_segment_size_even) // 2
    else:
        wall_is_even = 0
        half_wall_element_count_total = (wall_size - gate_segment_size_odd) // 2

    #########################################################################
    # We add the wall corner:
    #########################################################################

    generated_wall = generated_wall + wall_angle_id + '-'
    half_wall_element_count_processed = half_wall_element_count_processed + 1

    #########################################################################
    # We generate the first half of the wall:
    #########################################################################

    for i in range(1, half_wall_element_count_total):
        if (wall_tower_spacing_current == wall_tower_spacing_i) and ((half_wall_element_count_processed + 1) < half_wall_element_count_total) or (wall_tower_spacing_i == 0):
            # Wall tower:
            generated_wall = generated_wall + wall_tower_id + "-"
            half_wall_element_count_processed = half_wall_element_count_processed + 1
            wall_tower_spacing_current = 0
        else:
            # Wall straight:
            generated_wall = generated_wall + wall_straight_id + "-"
            half_wall_element_count_processed = half_wall_element_count_processed + 1
            wall_tower_spacing_current = wall_tower_spacing_current + 1
    
    #We save the symmetry of generated_wall:
    generated_wall_symmetry = generated_wall[::-1]

    #We Add the gate:
    if wall_is_even == 1:
        # Even
        generated_wall = generated_wall + generated_gate_even
    else:
        # Odd
        generated_wall = generated_wall + generated_gate_odd
    
    # We add the second half of the wall:
    generated_wall = generated_wall + generated_wall_symmetry

    f.write(str(wall_size) + ":" + generated_wall + "\n")

f.write(":endWallPaterns")
f.close()