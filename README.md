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

Detectnet_v2 requires kitti-formatted data to converted to TFRecords. The detectnet_v2 cli provides a 'dataset_convert' tool to do so. The detectnet_v2/specs/detectnet_v2_tfrecords_kitti_trainval.txt and ...\_test.txt are the configs for converting their respective datasets.

## Initial training

The detectnet_v2/specs/detectnet_v2_train_eval_config.txt contains all configuration for the initial training of the model, and the start_training.sh file starts the training process.

I mostly used the default settings provided in the **Creating a Configuration File** section of the TLT guide for my first run. I did need to update the labels to match mine of with_mask and without_mask. I also had to change the augmentation_config->preprocessing->enable_auto_resize flag to True, because my input images were not all the same shape.
