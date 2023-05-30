# **`Ancient Warfare Structures Scripts`**

This repository contains the scripts used to ease generating the structures for the `Ancient Warfare 2` Minecraft mod.


## Usage

The scripts are written in bash and require a bash shell to run. They are tested on `Linux`.  
They are meant to be run from the root of the repository.

---

# Script 1: `wood_converting_script.sh`

This script will convert an oak wood structure from the `structures` folder into all wood types from `Vanilla`, `Biomes O' Plenty` and `Rustic` mods.  
The new structures will be placed in the `structures` folder, organized in subfolders by mod name.

## Usage

With the desired structure(s) in the `structures` folder, run the script with the following command:

```
bash wood_converting_script.sh
```

The script will then generate the structure in all wood types. This totals to 24 structures per structure file in the `structures` folder.  
### Note:
- This script does not support fence gates
- This script does not support doors
- For your structure to be compatible with the script, make sure to name your structure so that it ends with `_oak`.
---

# Script 2: `town_wall_generator.sh`

This script will generate a town wall string for the `Ancient Warfare 2` town generator.

This script is used for `AW2 towns`, particularly `walled towns`. In the town's gen file, you are required to provide a "blueprint" for each size of the town's walls.  
This task is straightforward for towns with less than 7 walls, but it becomes confusing and tedious as the number of walls increases.

The purpose of this new script is to `generate blueprints for town walls` of any size in just a second. It offers modularity, allowing you to adjust the number of walls between two towers.  
You can also specify whether you want towers or walls on both sides of the gates. This functionality applies to town walls ranging from 3 walls in length up to an impressive 1000 walls or even more!

## Usage

Run the script with the following command:

```
bash town_wall_generator.sh $1 $2 $3
```

Where:

- `$1` is the minimum number of walls in the town wall blueprint.
- `$2` is the maximum number of walls in the town wall blueprint.
- `$3` is the number of walls between two towers.

The script will then generate a town wall blueprint for each size between the minimum and maximum number of walls.

<details>
    <summary>Click to reveal a usage example.</summary>
      
    bash town_wall_generator.sh 5 15 2  
      
    Will generate:  
      
    wallPatterns:
    5:0-5-2-5-0
    6:0-5-3-4-5-0
    7:0-1-5-2-5-1-0
    8:0-1-5-3-4-5-1-0
    9:0-1-1-5-2-5-1-1-0
    10:0-1-1-5-3-4-5-1-1-0
    11:0-1-1-1-5-2-5-1-1-1-0
    12:0-1-1-1-5-3-4-5-1-1-1-0
    13:0-1-1-5-1-5-2-5-1-5-1-1-0
    14:0-1-1-5-1-5-3-4-5-1-5-1-1-0
    15:0-1-1-5-1-1-5-2-5-1-1-5-1-1-0
    :endWallPaterns
</details>
<br>

Keep in mind that you can edit the `town_wall_generator.sh` script to change the default values for the `wall IDs`.  
There is also the `option to force or not walls or towers on both sides of the gates`.

<br>
<details>
    <summary>Click to reveal options.</summary>
      
    wall_gate_towers_odd=1
    wall_gate_towers_even=1

    #0: walls on each side of the gate
    #1: towers on each side of the gate
    #2: we don't care
</details>

<br>

The script will generate a `generated_walls.txt` file in the source folder.

---

# Planned features

- Make the scripts use `Python` instead of `bash`.
- Make `town_wall_generator.sh` not need editing.
