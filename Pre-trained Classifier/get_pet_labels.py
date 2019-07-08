from os import listdir
from os import path


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    filename_list = listdir(image_dir)
    for filename in filename_list:
        if filename.startswith("."):
            continue
        list_of_name_parts = path.splitext(filename)[0].lower().split("_")
        label = ""
        for name_part in list_of_name_parts:
            if name_part.isalpha():
                label += name_part + " "
        results_dic[filename] = [label.strip()]
    return results_dic
