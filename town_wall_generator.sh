# This script will generate AW structure town wall blueprint strings.


# Set the size of the wall to generate:
wall_size_start=$1
wall_size_end=$2

# Set the number of elements between 2 towers:
wall_tower_spacing=$3

#Set if we don't care, or want 2 towers or walls at the gate:
wall_gate_towers_odd=1
wall_gate_towers_even=1
#0: walls on each side of the gate
#1: towers on each side of the gate
#2: we don't care

# Set the wall element ids:
wall_angle_id=0
wall_straight_id=1
wall_gate_odd_id=2
wall_gate_even_left_id=3
wall_gate_even_right_id=4
wall_tower_id=5

echo "Generating walls from size $wall_size_start to $wall_size_end, with $wall_tower_spacing straight walls between 2 towers."

#We create or clean a file to store the generated walls:
echo "wallPatterns:" > generated_walls.txt

##############################################################################################################
# We check if parameters are correct:
##############################################################################################################

if [ $wall_size_start -lt 5 ]; then
    echo "Error: minimum ($1) must at least be 5."
    exit 1
fi
if [ $wall_size_end -lt $wall_size_start ]; then
    echo "Error: maximum ($2) must be greater than minimum ($1)."
    exit 1
fi
if [ $wall_tower_spacing -lt 0 ]; then
    echo "Error: tower spacing ($3) must be greater than 0."
    exit 1
fi


##############################################################################################################
# We generate the gate segments:
##############################################################################################################

# Odd gate:
if [ $wall_gate_towers_odd -eq 1 ]; then
    # We generate the gate with towers:
    generated_gate_odd="$wall_tower_id-$wall_gate_odd_id-$wall_tower_id"
    gate_segment_size_odd=3
else 
    if [ $wall_gate_towers_odd -eq 0 ]; then
        # We generate the gate with walls:
        generated_gate_odd="$wall_straight_id-$wall_gate_odd_id-$wall_straight_id"
        gate_segment_size_odd=3
    else
        # We generate the gate:
        generated_gate_odd="$wall_gate_odd_id"
        gate_segment_size_odd=1
    fi
fi

# Even gate:
if [ $wall_gate_towers_even -eq 1 ]; then
    # We generate the gate with towers:
    generated_gate_even="$wall_tower_id-$wall_gate_even_left_id-$wall_gate_even_right_id-$wall_tower_id"
    gate_segment_size_even=4
else 
    if [ $wall_gate_towers_even -eq 0 ]; then
        # We generate the gate with walls:
        generated_gate_even="$wall_straight_id-$wall_gate_even_left_id-$wall_gate_even_right_id-$wall_straight_id"
        gate_segment_size_even=4
    else
        # We generate the gate:
        generated_gate_even="$wall_gate_even_left_id-$wall_gate_even_right_id"
        gate_segment_size_even=2
    fi
fi

##############################################################################################################
# We generate the walls:
##############################################################################################################

for (( wall_size=$wall_size_start; wall_size<=$wall_size_end; wall_size++ ))
do
    # We generate the empty wall and reset the counters:
    generated_wall=""
    half_wall_element_count_processed=0
    wall_tower_spacing_current=0

    #########################################################################
    # We calculate the number of elements on each side of the gate:
    #########################################################################

    #Test if odd or even:
    if [ $((wall_size % 2)) -eq 0 ]; then
        wall_is_even=1
        half_wall_element_count_total=$(((wall_size - gate_segment_size_even) / 2))
    else
        wall_is_even=0
        half_wall_element_count_total=$(((wall_size - gate_segment_size_odd) / 2))
    fi

    #########################################################################
    # We add the wall corner:
    #########################################################################

    generated_wall="$generated_wall$wall_angle_id-"
    half_wall_element_count_processed=$((half_wall_element_count_processed + 1))

    #########################################################################
    # We generate the first half of the wall:
    #########################################################################

    for (( i=1; i<$half_wall_element_count_total; i++ ))
    do

        if ([ $wall_tower_spacing_current -eq $wall_tower_spacing ] && [ $(($half_wall_element_count_processed + 1)) -lt $half_wall_element_count_total ]) || [ $wall_tower_spacing -eq 0 ]; then
            # Wall tower:
            generated_wall="$generated_wall$wall_tower_id-"
            half_wall_element_count_processed=$((half_wall_element_count_processed + 1))
            wall_tower_spacing_current=0
        else
            # Wall straight:
            generated_wall="$generated_wall$wall_straight_id-"
            half_wall_element_count_processed=$((half_wall_element_count_processed + 1))
            wall_tower_spacing_current=$((wall_tower_spacing_current + 1))
        fi
    done

    #We save the symmetry of $generated_wall:
    generated_wall_symmetry=$(echo $generated_wall | rev)

    # We add the gate:
    if [ $wall_is_even -eq 1 ]; then
        # Even
        generated_wall="$generated_wall$generated_gate_even"
    else
        # Odd
        generated_wall="$generated_wall$generated_gate_odd"
    fi

    # We add the second half of the wall:
    generated_wall="$generated_wall$generated_wall_symmetry"

    echo "$wall_size:$generated_wall">> generated_walls.txt
done

echo ":endWallPaterns">> generated_walls.txt
