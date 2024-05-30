#!/usr/bin/env python3
import argparse
from modules.convolve import *
from modules.invert import *
from modules.ttohsl import *
import numpy as np
from skimage import util, io, exposure

parser = argparse.ArgumentParser(description="A quick app to invert the black/white background whithout changing original color")

parser.add_argument('-i', "--input", type=str, help="input image path")
parser.add_argument("-o", "--output", type=str, help="output image path, default is output.png", default='output.png')
parser.add_argument("-s", "--colorspace", type=str, choices=['hsl', 'lab', 'yiq'], help="hsl/lab/yiq, default is hsl", default='hsl')
parser.add_argument("-k", "--kernel", type=str, choices=['blur', 'sharpen', 'edge', None], help="blur/sharpen/edge,default is None",default=None)
parser.add_argument("-g", "--gamma", type=float, help="a float equal to gamma value, default is 1", default=1)

args = parser.parse_args()

if not args.input:
    parser.error("The --input argument is required.")

conversion_funcs = {
    'rgb': util.invert,
    'hsl': invert_hls,
    'yiq': invert_yiq,
    'lab': invert_lab
}

def main(input, output, colorspace, kernel, gamma):
    path = input
    image_data = np.array(io.imread(path))

    negative_image = invert(image_data, colorspace, kernel)

    negative_image = exposure.adjust_gamma(ensure_non_negative(negative_image), gamma=gamma)

    io.imsave(f"{output}", util.img_as_ubyte(negative_image))
    print(f'Inverted! image saved at "{output}"')

def invert(input, colorspace, kernel):
    image_data = input[:, :, :3]

    if kernel != None:
        image_data_kernel = apply_kernel(image_data, kernel)
    else:
        image_data_kernel = image_data.copy()

    image_data_kernel = np.clip(image_data_kernel, 0, 255)
    image_data_kernel = util.img_as_ubyte(image_data_kernel / 255.0)

    conversion_func = conversion_funcs.get(colorspace, None)
    negative_image = conversion_func(image_data_kernel)

    return negative_image

def ensure_non_negative(image):
    return exposure.rescale_intensity(image, out_range=(0, 1))

main(args.input, args.output, args.colorspace, args.kernel, args.gamma)
