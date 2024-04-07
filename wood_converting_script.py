import os
import shutil

# This script will generate Ancient Warfare structures from oak to all wood types, vanilla, rustic, and biome's o plenty.

# We make our local variables:

original_wood_type = "oak"

# We will divide the process into several functions:


# cleaning up and creation of the local folders
def cleanup_folder(new_mod_id):
    # If the ./structures/ folder does not exist, we will create it.
    if not os.path.exists("./structures/"):
        os.mkdir("./structures/")
        print("Created folder ./structures/")

    # If the ./structures/$1/ folder does not exist, we will create it. If it does, we will clean it up.
    if not os.path.exists(f"./structures/{new_mod_id}/"):
        os.mkdir(f"./structures/{new_mod_id}/")
        print(f"Created folder ./structures/{new_mod_id}/")
    else:
        print(f"Folder ./structures/{new_mod_id}/ already exists. Cleaning it up...")
        shutil.rmtree(f"./structures/{new_mod_id}/*")


# copying the files from the template folder to the new folder
def copy_files(new_mod_id):
    # We only clone the files whose name finishes with the original wood type.
    for file_name in os.listdir("./templates/"):
        if original_wood_type in file_name:
            shutil.copy(f"./templates/{file_name}", f"./structures/{new_mod_id}/")
    # print("Cloned template structures from ./templates/ to ./structures/$new_mod_id/")


# renaming the structures
def rename_structures(new_mod_id, new_wood_type):
    # We rename the structures: file name and "name" tag.
    for file_name in os.listdir(f"./structures/{new_mod_id}/"):
        if original_wood_type in file_name:
            with open(f"./structures/{new_mod_id}/{file_name}", "r") as file:
                content = file.read()
            content = content.replace(original_wood_type, new_wood_type)
            with open(f"./structures/{new_mod_id}/{file_name}", "w") as file:
                file.write(content)
            os.rename(f"./structures/{new_mod_id}/{file_name}", f"./structures/{new_mod_id}/{file_name.replace(original_wood_type, new_wood_type)}")
    # print(f"Renamed structures for {new_wood_type}")


# adding the mod dependency
def add_mod_id(new_mod_id, new_wood_type):
    if new_wood_type != "vanilla":
        for file_name in os.listdir(f"./structures/{new_mod_id}/"):
            with open(f"./structures/{new_mod_id}/{file_name}", "r") as file:
                content = file.read()
            content = content.replace('mods=', 'mods=' + new_wood_type)
            with open(f"./structures/{new_mod_id}/{file_name}", "w") as file:
                file.write(content)
        # print(f"Added {new_wood_type} mod dependency to {new_wood_type} structure files.")


def change_wood_variant(new_mod_id, new_wood_type):
    for file_name in os.listdir(f"./structures/{new_mod_id}/"):
        if original_wood_type in file_name:
            with open(f"./structures/{new_mod_id}/{file_name}", "r") as file:
                content = file.read()
            content = content.replace(f"variant:{original_wood_type}", f"variant:{new_wood_type}")
            content = content.replace(f'variant:"{original_wood_type}"', f'variant:"{new_wood_type}"')
            with open(f"./structures/{new_mod_id}/{file_name}", "w") as file:
                file.write(content)
    # print(f"Changed {new_wood_type} wood variant to {new_wood_type}. Original wood type was {original_wood_type}.")


# You can continue defining other functions similarly.

# Main script starts here:

#############################################################################################################
# Vanilla wood types:
#############################################################################################################

new_mod_id = "vanilla"

cleanup_folder(new_mod_id)
for new_wood_type in ["birch", "spruce", "jungle", "acacia", "dark_oak"]:
    copy_files(new_mod_id)
    rename_structures(new_mod_id, new_wood_type)
    change_wood_variant(new_mod_id, new_wood_type)
    # Add other function calls accordingly
    print(f"Done generating all structures with with {new_wood_type}")
copy_files(new_mod_id)  # We copy the oak files again, because we still want them.
print("Done generating all structures with with oak")

# You can continue with Rustic wood types and Biomes O' Plenty wood types similarly.
