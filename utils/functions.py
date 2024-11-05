import os
import matplotlib.pyplot as plt

def create_folder(path):
    folder = ""
    back_folders = path.split("/")[:-1]
    for iter_folder in back_folders:
        if iter_folder == back_folders[0]:
            folder = iter_folder
        else:
            folder = f"{folder}/{iter_folder}"
    if not os.path.isdir(folder):
        os.makedirs(folder)


def custom_save_fig(path):
    create_folder(path)
    plt.savefig(path, format="png", dpi=300, bbox_inches="tight")


def custom_save_dict(dict, path):
    create_folder(path)
    with open(path, "w") as file:
        file.write(str(dict))


