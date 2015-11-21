# coding: utf-8

import random

import numpy as np
"""
TODO: Comment in
import caffe
"""
from PIL import Image


def load_image(fpath):
    image = Image.open(fpath, 'r').convert('RGB')

    image = image.resize((256, 256), Image.BILINEAR)

    left = 256 - 227 / 2
    upper = 256 - 227 / 2
    right = left + 227
    lower = upper + 227
    image = image.crop((left, upper, right, lower))

    r, g, b = image.split()
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)

    data = np.zeros((3, 227, 227))
    data[0, :, :] = b
    data[1, :, :] = g
    data[2, :, :] = r

    return data


def make_code(net, data):
    # TODO: Erase dummy code
    code = [float(random.randint(0, 1)) for i in range(48)]

    """
    TODO: Comment in
    net.blobs['data'].reshape(1, 3, 227, 227)
    net.blobs['data'].data[...] = data
    output = net.forward()
    code = output['fc8_kevin_encode']

    for i in range(len(code)):
        if code[i] >= 0.5:
            code[i] = 1
    """

    return code
