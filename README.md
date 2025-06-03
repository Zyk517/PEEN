# PEEN
The paper "Probability-Guided Edge Enhancement Network for Remote Sensing Image Semantic Segmentation "implementation code.

# Usage
## Requirements
Before training, carefully check whether your format meets the requirements. The library requires that the data set format is VOC format. The content that needs to be prepared is input pictures and labels.

The label is a png image. Since the ISPRS dataset was downloaded from the Internet, the label format does not match and needs to be reprocessed. Be sure to pay attention! The value of each pixel of the label is the type to which this pixel belongs. It needs to be changed to: the pixel value of the background is 0 and the pixel value of the target is other.

First, the ISPRS Vaihingen and Potsdam datasets are required. A link is provided here for download.
https://gitcode.com/Premium-Resources/43a42/?utm_source=article_gitcode_universal&index=top&type=card&

Then we need to use labelme to process the label file into a runnable format. The reference method is the json_to_dataset.py file. The recommended version of labelme is 3.16.7.

Next, the data set needs to be divided into the training set and the test set. The voc_annotation.py file can be used for the division and stored respectively in the corresponding folders in the Datesets.

Finally, the logs file contains the trained model weight file best_epoch_weights.pth. However, due to its large size, it has been shared separately in the link for download.

Files shared via cloud disk: best_epoch_weights.pth
Link：https://pan.baidu.com/s/1t4n1BK55jIFRg44ZFnzE8AE](https://pan.baidu.com/s/1ZTrnihyarBHlAOQEMgOEdg?pwd=aumu xtraction code:aumu

## Noting
The training weights are trained using an image size of 256×256. If they are to be used, it is best to use the same size as well.
