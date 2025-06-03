import time
import cv2
import torch
import numpy as np
from util.config import config as cfg
from util.misc import fill_hole
from skimage import segmentation


def PF_alpha(x, k):
    betak = (1 + np.exp(-k)) / (1 - np.exp(-k))
    dm = max(np.max(x), 0.0001)
    res =1- (2 / (1 + np.exp(-x * k / dm)) - 1) * betak
    return np.maximum(0, res)


def get_contours(preds):

    binary_image = (preds >= threshold).astype(np.uint8)


    kernel = np.ones((5, 5), np.uint8)
    binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)


    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def get_min_distances(contours, image_shape):
    min_distances = []
    R = 0

    for contour_idx, contour in enumerate(contours):
        mask = np.zeros(image_shape, dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

        for other_contour_idx, other_contour in enumerate(contours):
            if other_contour_idx != contour_idx:
                cv2.drawContours(mask, [other_contour], -1, 0, thickness=cv2.FILLED)

        distance_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 3)

        min_distance = np.min(distance_transform[mask == 255])

        min_distances.append(min_distance)

        R = max(R, min_distance)

    return min_distances, R

























