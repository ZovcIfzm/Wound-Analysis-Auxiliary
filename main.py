import glob
import argparse

import cv2

import constants as k
import masking as masking

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='CreateLabels')
    parser.add_argument('--img_dir', type=str, required=True, default="images/" help='Path to images directory')
    parser.add_argument('--apply_mask', type=str, required=False, default=False help='Apply masking to defualt images T/F')
    parser.add_argument('--output_dir', type=str, required=False, default="images/", help='Path to output directory')
    args = parser.parse_args()

    # read in images
    filenames = [img for img in glob.glob(args.img_dir)]
    images = []
    for img in filenames:
        n = cv2.imread(img)
        images.append(n)

    # CONDITIONALLY apply mask
    if args.apply_mask:
        for i in range(len(images)):
            images[i] = masking.apply_mask(k.LR, k.UR, images[i])

    for i in range(len(images)):
        cv2.imwrite(args.output_dir + filenames[i], images[i])

    # CONDITIONALLY augment data