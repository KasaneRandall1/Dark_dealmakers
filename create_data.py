import json
import os
import imghdr


def player_cards():
    def grab_images_from_folder(folder_path):
        image_files = []

        # Traverse through the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Check if the file is an image
                file_path = os.path.join(root, file)
                if is_image_file(file_path):
                    image_files.append(file)

        return image_files

    def is_image_file(file_path):
        # Check if the file is an image using imghdr
        image_type = imghdr.what(file_path)
        return image_type is not None

    # Example usage
    folder_path = "img/player_creature/"
    image_files = grab_images_from_folder(folder_path)

    card_list = []
    x = 0
    while len(card_list) < len(image_files):
        cards = {
        "img_path":image_files[x]
    }
        card_list.append(cards)
        x += 1

    with open("data/player_cards.json","x") as i:
        json.dump(card_list,i,indent=4)

def cpu_cards():
    def grab_images_from_folder(folder_path):
        image_files = []

        # Traverse through the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Check if the file is an image
                file_path = os.path.join(root, file)
                if is_image_file(file_path):
                    image_files.append(file)

        return image_files

    def is_image_file(file_path):
        # Check if the file is an image using imghdr
        image_type = imghdr.what(file_path)
        return image_type is not None

    # Example usage
    folder_path = "img/cpu_creature/"
    image_files = grab_images_from_folder(folder_path)

    card_list = []
    x = 0
    while len(card_list) < len(image_files):
        cards = {
        "img_path":image_files[x]
    }
        card_list.append(cards)
        x += 1

    with open("data/cpu_cards.json","x") as i:
        json.dump(card_list,i,indent=4)

player_cards()
cpu_cards()
