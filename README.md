# mask-detect-tlt


This project prepares the included dataset for Nvidia's transfer learning
toolkit, specifically object detection using Detectnet_v2

I used the dataset provided here: https://www.pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/

I used this tool to annotate the dataset in kitti format: https://github.com/SaiPrajwal95/annotate-to-KITTI

I followed the steps to build a model from Nvidia's Transfer Learning Toolkit (TLT) provided here: https://docs.nvidia.com/tlt/tlt-user-guide/text/object_detection/detectnet_v2.html#data-input-for-object-detection

I also used this project from Nvidia's AI-IOT collection, mostly as reference for config files: https://github.com/NVIDIA-AI-IOT/face-mask-detection

## Preparing data for training

I used the kitti-annotation to generate the bounding box labels and wrote the helpers/split_kitty.py to randomly split the dataset into train and test, defaulting to an 80/20 split.

## Re-converting for ingestion by DetectNet_v2

Detectnet_v2 requires kitti-formatted data to be converted to TFRecords. The detectnet_v2 cli provides a 'dataset_convert' tool to do so. The detectnet_v2/specs/detectnet_v2_tfrecords_kitti_trainval.txt and ...\_test.txt are the configs for converting their respective datasets.

## Initial training

The detectnet_v2/specs/detectnet_v2_train_eval_config.txt contains all configuration for the initial training of the model, and the start_training.sh file starts the training process.

I mostly used the default settings provided in the **Creating a Configuration File** section of the TLT guide for my first run. I did need to update the labels to match mine of with_mask and without_mask. I also had to change the augmentation_config->preprocessing->enable_auto_resize flag to True, because my input images were not all the same shape.

## First evaluation

The start_eval.sh file will run the evaluation on the test set. My initial run gives suspiciously high precision:

|class name   | average precision (in %)|
|-------------|-------------------------|
|with_mask    | 98.9032                 |
|without_mask | 99.2055                 |

But this may be also explained by the dataset. The 'with_mask' images are just normal images of faces with the same image of a mask superimposed over the mouth & nose region based on facial landmark detection. The dataset was generated early in the covid period, so there weren't as many actual images of masked faces available. Future iterations of this project will use better data. 

## Running inference

The run_inference.sh file contains the command to run the model on the test set and draw bounding boxes around detected with_mask and without_mask areas. It uses the detectnet_v2/specs/detectnet_v2_inference_config.txt file.

After running inference the first time, all examples I checked were boxed correctly, but that there were many false-positive boxes drawn along with the correct ones. For example, in the data/inference_on_test folder, the image for mask_34-with-mask shows 2 boxes, one red and one green. Checking the corresponding txt file (in the labels folder), I can see that with_mask got a much higher score of 37.341, compared to without_mask's score of 1.677. I found that updating the dbscan_confidence_threshold from 0.9 to 5.0, I was able to eliminate most of the false positives.

## Pruning, retraining, and exporting 

I followed the walkthrough for pruning and retraining and got similar success. I exported the model to a .etlt file. 

## Next steps

1. Plug a model I've trained into the python-deepstream demo. This will allow me to assess how it functions in video. It is also more directly applicable for the LENS project.
1. Collect more data.
  1. I could use actual masked photos and run them against my current model to see how well the overlay mask actually simulates reality. 
  1. I can also use actual masked photos for training.
  1. I'd like to take some photos of people in masks around Seagate to supply some additional training material.