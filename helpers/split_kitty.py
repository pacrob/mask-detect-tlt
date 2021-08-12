import os
from random import shuffle
from math import floor
import argparse
from shutil import copyfile

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True,
	help="path to data folder")
ap.add_argument("-i", "--images", type=str, default="images",
	help="name of images folder")
ap.add_argument("-l", "--labels", type=str, default="labels",
	help="name of labels folder")
ap.add_argument("-s", "--split", type=int, default=20,
	help="percent to of files to use as test"),

args = vars(ap.parse_args())

def get_file_list_from_dir(datadir):
    all_files = list(os.listdir(os.path.abspath(datadir)))
    return all_files

def strip_extensions_from_file_list(file_list):
    stripped_files = list(map((lambda x: os.path.splitext(x)[0]), file_list))
    return stripped_files

def get_extension_from_files(file_list):
    extension = os.path.splitext(file_list[0])[1]
    return extension

def randomize_files(file_list):
    shuffle(file_list)

def get_training_and_testing_sets(file_list):
    # convert percent to decimal
    split = args["split"] / 100
    split_index = floor(len(file_list) * split)
    testing = file_list[:split_index]
    training = file_list[split_index:]
    return training, testing

def create_folders_for_test_train_files():
    try:
        os.makedirs(os.path.join(args["data"], "train", args["images"]))
        os.makedirs(os.path.join(args["data"], "train", args["labels"]))
        os.makedirs(os.path.join(args["data"], "test", args["images"]))
        os.makedirs(os.path.join(args["data"], "test", args["labels"]))
    except OSError as error:
        print('error creating test and train dirs - do they already exist?')

def copy_files_into_train_test_folders(test_list, train_list, image_ext, label_ext, args):
    for file in test_list:
        full_image_name = f'{file}{image_ext}'
        full_label_name = f'{file}{label_ext}'
        copyfile(f'{args["data"]}/{args["images"]}/{full_image_name}', 
                 f'{args["data"]}/test/{args["images"]}/{full_image_name}')
        copyfile(f'{args["data"]}/{args["labels"]}/{full_label_name}', 
                 f'{args["data"]}/test/{args["labels"]}/{full_label_name}')

    for file in train_list:
        full_image_name = f'{file}{image_ext}'
        full_label_name = f'{file}{label_ext}'
        copyfile(f'{args["data"]}/{args["images"]}/{full_image_name}', 
                 f'{args["data"]}/train/{args["images"]}/{full_image_name}')
        copyfile(f'{args["data"]}/{args["labels"]}/{full_label_name}', 
                 f'{args["data"]}/train/{args["labels"]}/{full_label_name}')

# get a list of files from the images dir
image_files = get_file_list_from_dir(os.path.join(args["data"], args["images"]))
label_files = get_file_list_from_dir(os.path.join(args["data"], args["labels"]))
# get extensions
image_ext = get_extension_from_files(image_files)
label_ext = get_extension_from_files(label_files)
# strip the extensions off
no_ext_image_files = strip_extensions_from_file_list(image_files)
no_ext_label_files = strip_extensions_from_file_list(label_files)
# verify each image has a label
if set(no_ext_image_files) != set(no_ext_label_files):
    print('images and labels lists do not match')
    exit(1)
# randomize order
randomize_files(no_ext_image_files)
# split randomized list into train and test lists
train, test = get_training_and_testing_sets(no_ext_image_files)
# create all 4 folders
create_folders_for_test_train_files()
# copy appropriate files into the 4 folders
copy_files_into_train_test_folders(test, train, image_ext, label_ext, args)



print('train' + str(len(train)))
print('test' + str(len(test)))
print('image ext ' + image_ext)
print('label ext ' + label_ext)

# x = list(range(10))
# a, b = get_training_and_testing_sets(x)
# print(a)
# print(b)


