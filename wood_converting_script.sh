#This script will generate Ancient Warfare structures from oak to all wood types, vanilla, rustic, and biome's o plenty.

#We make our local variables:

original_wood_type="oak"

#We will divide the process in several steps:


#cleaning up and creation of the local folders
function cleanup_folder {
    
    #If the ./structures/ folder does not exist, we will create it.
    if [ ! -d ./structures/ ]; then
        mkdir ./structures/
        echo "Created folder ./structures/"
    fi

    #If the ./structures/$1/ folder does not exist, we will create it. If it does, we will clean it up.
    if [ ! -d ./structures/$1/ ]; then
        mkdir ./structures/$1/
        echo "Created folder ./structures/$1/"
        else
        echo "Folder ./structures/$1/ already exists. Cleaning it up..."
        rm -rf ./structures/$1/*
    fi
}

#copying the files from the template folder to the new folder
function copy_files {
    #We only clone the files whose name finishes with the original wood type.
    cp ./templates/*$original_wood_type* ./structures/$new_mod_id/ 2> /dev/null
    #echo "Cloned template structures from ./templates/ to ./structures/$new_mod_id/"
}

#renaming the structures
function rename_structures {
    #We rename the structures: file name and "name" tag.
    for file in structures/$new_mod_id/*$original_wood_type*; do
        sed -i "/^name=/ s/$original_wood_type/$1/g" "$file"; #We replace the "name=" tag.
        mv "$file" "${file/$original_wood_type/$1}"; #We rename the file.
    done
    #echo "Renamed structures for $1"
}

#adding the mod dependancy
function add_mod_id {
    if [ $1 != "vanilla" ]; then
        for file in structures/$new_mod_id/*; do sed -i 's/mods='.*'/mods='$1'/g' "$file"; done
        #echo "Added "$1" mod dependancy to "$new_wood_type" structure files."
    fi
}


function change_wood_variant {

    for file in structures/$new_mod_id/*$1*; do 
        sed -i 's/variant:'$original_wood_type'/variant:'$1'/g' "$file";
        sed -i 's/variant:"'$original_wood_type'"/variant:"'$1'"/g' "$file";
        
    done

    #echo "Changed $2 wood variant to $1. Orginal wood type was $original_wood_type."
}

function change_slab_id {
    if [ $2 == "rustic" ]; then
        for file in structures/$new_mod_id/*$1*; do 
            sed -i 's/minecraft:wooden_slab/'$2':'$1'_slab/g' "$file";
            sed -i 's/,variant:"'$1'"//g' "$file";
        done
        #echo "Changed slab block ID for $2 wood variant $1."
    fi

    if [ $2 == "biomesoplenty" ]; then
        for file in structures/$new_mod_id/*$1*; do
            if [ $1 = "sacred_oak" ] || [ $1 = "cherry" ] || [ $1 = "umbran" ] || [ $1 = "fir" ] || [ $1 = "ethereal" ] || [ $1 = "magic" ] || [ $1 = "mangrove" ] || [ $1 = "palm" ]; then
                sed -i 's/minecraft:wooden_slab/'$2':wood_slab_0/g' "$file";
            fi
            if [ $1 = "redwood" ] || [ $1 = "willow" ] || [ $1 = "pine" ] || [ $1 = "hellbark" ] || [ $1 = "jacaranda" ] || [ $1 = "mahogany" ] || [ $1 = "ebony" ] || [ $1 = "eucalyptus" ]; then

                sed -i 's/minecraft:wooden_slab/'$2':wood_slab_1/g' "$file";
            fi
        done
        #echo "Changed slab block ID for $2 wood variant $1."
    fi
}

function change_log_id {

    if [ $2 = "vanilla" ]; then
        if [ $1 = "dark_oak" ] || [ $1 = "acacia" ]; then
            for file in structures/$new_mod_id/*$1*; do sed -i 's/log/log2/g' "$file"; done
            #echo "Changed log block ID for $2 wood variant $1."
        fi
    fi

    if [ $2 = "biomesoplenty" ]; then
        if [ $1 = "sacred_oak" ] || [ $1 = "cherry" ] || [ $1 = "umbran" ] || [ $1 = "fir" ]; then

            for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:log/'$2':log_0/g' "$file"; done
        fi
        if [ $1 = "ethereal" ] || [ $1 = "magic" ] || [ $1 = "mangrove" ] || [ $1 = "palm" ]; then

            for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:log/'$2':log_1/g' "$file"; done
        fi
        if [ $1 = "redwood" ] || [ $1 = "willow" ] || [ $1 = "pine" ] || [ $1 = "hellbark" ]; then

            for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:log/'$2':log_2/g' "$file"; done
        fi
        if [ $1 = "jacaranda" ] || [ $1 = "mahogany" ] || [ $1 = "ebony" ] || [ $1 = "eucalyptus" ]; then

            for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:log/'$2':log_3/g' "$file"; done
        fi
    fi

    if [ $2 != "vanilla" ] && [ $2 != "biomesoplenty" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:log/'$2':log/g' "$file"; done
    fi
}

function change_plank_id {

    if [ $2 = "biomesoplenty" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:planks/'$2':planks_0/g' "$file"; done
    else if [ $2 != "vanilla" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:planks/'$2':planks/g' "$file"; done
    fi
    fi
}

function change_fence_id {
    if [ $2 == "rustic" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:fence/'$2':fence_'$1'/g' "$file"; done
    fi
    if [ $2 == "vanilla" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:fence/minecraft:'$1'_fence/g' "$file"; done
    fi
    if [ $2 == "biomesoplenty" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:fence/'$2':'$1'_fence/g' "$file"; done
    fi
}

function change_stairs_id {
    if [ $2 == "rustic" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:oak_stairs/'$2':stairs_'$1'/g' "$file"; done
    fi
    if [ $2 == "vanilla" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:oak_stairs/minecraft:'$1'_stairs/g' "$file"; done
    fi
    if [ $2 == "biomesoplenty" ]; then
        for file in structures/$new_mod_id/*$1*; do sed -i 's/minecraft:oak_stairs/'$2':'$1'_stairs/g' "$file"; done
    fi
}

#############################################################################################################
# Vanilla wood types:
#############################################################################################################

new_mod_id="vanilla"

cleanup_folder $new_mod_id
for new_wood_type in birch spruce jungle acacia dark_oak; do
    copy_files
    rename_structures $new_wood_type
    change_wood_variant $new_wood_type $new_mod_id
    change_log_id $new_wood_type $new_mod_id
    change_fence_id $new_wood_type $new_mod_id
    change_stairs_id $new_wood_type $new_mod_id
    echo "Done generating all structures with with $new_wood_type"
done
copy_files #We copy the oak files again, because we still want them.
echo "Done generating all structures with with oak"


#############################################################################################################
# Rustic wood types:
#############################################################################################################

new_mod_id="rustic"

cleanup_folder $new_mod_id
for new_wood_type in olive ironwood; do
    copy_files
    rename_structures $new_wood_type
    add_mod_id $new_mod_id
    change_wood_variant $new_wood_type  $new_mod_id
    change_log_id $new_wood_type $new_mod_id
    change_slab_id $new_wood_type $new_mod_id
    change_plank_id $new_wood_type $new_mod_id
    change_fence_id $new_wood_type $new_mod_id
    change_stairs_id $new_wood_type $new_mod_id
    echo "Done generating all structures with with $new_wood_type"
done


#############################################################################################################
# Biomes O' Plenty wood types:
#############################################################################################################

new_mod_id="biomesoplenty"

cleanup_folder $new_mod_id
for new_wood_type in cherry umbran fir ethereal magic mangrove palm redwood willow pine hellbark jacaranda mahogany ebony eucalyptus sacred_oak; do
    copy_files
    rename_structures $new_wood_type
    add_mod_id $new_mod_id
    change_wood_variant $new_wood_type  $new_mod_id
    change_log_id $new_wood_type $new_mod_id
    change_slab_id $new_wood_type $new_mod_id
    change_plank_id $new_wood_type $new_mod_id
    change_fence_id $new_wood_type $new_mod_id
    change_stairs_id $new_wood_type $new_mod_id
    echo "Done generating all structures with with $new_wood_type"
done

