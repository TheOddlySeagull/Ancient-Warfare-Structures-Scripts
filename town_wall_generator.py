# This script will generate AW structure town wall blueprint strings.

import sys

wall_size_start_i = 0
wall_size_end_i = 0
wall_tower_spacing_i = 0
wall_size_start_s = str(wall_size_start_i)
wall_size_end_s = str(wall_size_end_i)
wall_tower_spacing_s = str(wall_tower_spacing_i)

# Set if the gate has towers or not:
wall_gate_towers_odd = 1
wall_gate_towers_even = 1

# Set the wall element ids:
wall_angle_id = '0'
wall_straight_id = '1'
wall_gate_odd_id = '2'
wall_gate_even_left_id = '3'
wall_gate_even_right_id = '4'
wall_tower_id = '5'

##############################################################################################################
# Function to ask the user for the wall element ids:
##############################################################################################################

def AskWallIDs():

    global wall_angle_id, wall_straight_id, wall_gate_odd_id, wall_gate_even_left_id, wall_gate_even_right_id, wall_tower_id

    print("Current wall element ids:")
    print("Angle: " + wall_angle_id)
    print("Straight: " + wall_straight_id)
    print("Gate (odd): " + wall_gate_odd_id)
    print("Gate (even, left): " + wall_gate_even_left_id)
    print("Gate (even, right): " + wall_gate_even_right_id)
    print("Tower: " + wall_tower_id)

    print("Do you want to change the wall element ids? (y/n)")
    change_wall_element_ids = input()
    if change_wall_element_ids == 'y':

        # We ask the user for the wall element ids:
        wall_angle_id = input("Enter the wall angle element id: ")
        wall_straight_id = input("Enter the wall straight element id: ")
        wall_gate_odd_id = input("Enter the wall gate element id (odd): ")
        wall_gate_even_left_id = input("Enter the wall gate element id (even, left): ")
        wall_gate_even_right_id = input("Enter the wall gate element id (even, right): ")
        wall_tower_id = input("Enter the wall tower element id: ")

##############################################################################################################
# Function to ask the user for the wall sizes:
##############################################################################################################

def AskWallSizes():

    global wall_size_start_i, wall_size_end_i, wall_tower_spacing_i, wall_size_start_s, wall_size_end_s, wall_tower_spacing_s

    # We ask the user for the wall sizes:
    wall_size_start_s = input("Enter the minimum wall size (must be at least 5): ")
    wall_size_end_s = input("Enter the maximum wall size (must be greater than minimum): ")
    wall_size_start_i = int(wall_size_start_s)
    wall_size_end_i = int(wall_size_end_s)
    # We ask the user for the number of elements between 2 towers:
    wall_tower_spacing_s = input("Enter the number of straight walls between 2 towers (must be greater than 0): ")
    wall_tower_spacing_i = int(wall_tower_spacing_s)

    # We check if parameters are correct:
    CheckSizes()

##############################################################################################################
# Function to ask the user the gate details:
##############################################################################################################

def AskGateDetails():
    
    global wall_gate_towers_odd, wall_gate_towers_even

    print("Currently, the script will generate 2 towers at the gates (odd and even).")
    print("Do you want to change this? (y/n)")
    change_gate_details = input()
    if change_gate_details == 'y':
        print("Use 0 for walls on each side of the gate, 1 for towers on each side of the gate, or 2 if you don't care.")
        wall_gate_towers_odd = input("Enter the gate details for odd walls: ")
        wall_gate_towers_even = input("Enter the gate details for even walls: ")


##############################################################################################################
# We check if parameters are correct:
##############################################################################################################

def CheckSizes():

    global wall_size_start_i, wall_size_end_i, wall_tower_spacing_i, wall_size_start_s, wall_size_end_s, wall_tower_spacing_s

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
# We ask the user for the wall sizes:
##############################################################################################################

AskWallSizes()
AskWallIDs()
AskGateDetails()

print("Generating walls from size " + wall_size_start_s + " to " + wall_size_end_s + ", with " + wall_tower_spacing_s + " straight walls between 2 towers.")

#We create or clean a file called "generated_walls.txt" to store the generated walls:
f = open("generated_walls.txt", "w")
f.write("wallPatterns:\n")


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