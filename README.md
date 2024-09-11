# Image Upscaler
My shot at a simple CNN applied to an image upscaler.


## Spec Targets
- Accepts images of any size (min/max to come with model goals)
- Photographs only (no cartoon, etc will be added - at first)
- 1000 unique images is ideal. Various sizes, shapes, colors is ideal.
    - can come from online datasets or web crawling
- Simple CNN
- No particular parameter goal - but should train on CPU.

## Image Choice
- The images are from the [Fruit Images for Object Detection](https://www.kaggle.com/datasets/mbkinaci/fruit-images-for-object-detection) dataset off of Kaggle.
![alt text](data\test_zip\test\apple_77.jpg)

## Image Prep
- Each of the images will be downscaled into half-resolution images.
    - simple scaling of the image. Break into 2x2 segments and take average of the pixels to create one pixel in output image.
- Each downscaled image will be broken into 8x8 sections (at random, 100 per image is ideal) and will be labeled with a 4x4 center output.
    - The 2x2 section that ends up in center of 8x8 will be upscaled to the 4x4 center.

## Model
- Not decided yet...