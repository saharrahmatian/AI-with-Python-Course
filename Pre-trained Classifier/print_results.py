def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    n_images = results_stats_dic.get("n_images")
    print("{} is the model we will be using\n".format(model))
    print("Number of Images= {}\n".format(n_images))
    print("Number of Dog Images= {}\n".format(results_stats_dic.get("n_dogs_img")))
    print("Number of 'Not-a' Images= {}\n".format(results_stats_dic.get("n_notdogs_img")))
    print("% Correct Dogs= {}\n".format(results_stats_dic.get("pct_correct_dogs")))
    print("% Correct Breed= {}\n".format(results_stats_dic.get("pct_correct_breed")))
    print("% Correct 'Not-a' Dog= {}\n".format(results_stats_dic.get("pct_correct_notdogs")))
    print("% Match= {}\n".format(results_stats_dic.get("pct_match")))

    n_correct_dogs = results_stats_dic.get("n_correct_dogs")
    n_correct_notdogs = results_stats_dic.get("n_correct_notdogs")
    n_correct_breed = results_stats_dic.get("n_correct_breed")

    if print_incorrect_dogs == True and n_correct_dogs + n_correct_notdogs != n_images:
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Misclassified dog, The pet label is: {} and classifier label is :{}"
                      .format(results_dic[key][0], results_dic[key][1]))

    if print_incorrect_breed == True and n_correct_dogs != n_correct_breed:
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Misclassified breed, The pet label is: {} and classifier label is :{}"
                      .format(results_dic[key][0], results_dic[key][1]))
