#################################################################
# FILE : cartoonify.py
# WRITER : yoav schneider , yoav.schneider , 313594087
# EXERCISE : intro2cs2 ex4 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: yonatan levy, shir giat, eldad eliyahu, gabriel dubin, achsaf atzmon
# WEB PAGES I USED:
# NOTES:
#################################################################

import copy
import ex5_helper
import math
import sys


def create_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append([])
    return matrix


def separate_channels(image):
    channel_list = []
    for channel_index in range(len(image[0][0])):
        channel_list += [make_channel(image, channel_index)]
    return channel_list


def make_channel(image, r0g1b2):
    matrix = create_matrix(len(image), 0)
    for row_index in range(len(image)):
        for pixel_index in range(len(image[0])):
            matrix[row_index].append(image[row_index][pixel_index][r0g1b2])
    return matrix
# ----separate channels----


def combine_channels(channels):
    matrix = create_matrix(len(channels[0]), len(channels[0][0]))
    for row_index in range(len(channels[0])):
        for pixel_index in range(len(channels[0][0])):
            for channel_index in range(len(channels)):
                matrix[row_index][pixel_index].append(channels[channel_index][row_index][pixel_index])
    return matrix
# ----combine channels----


def RGB2grayscale(colored_image):
    matrix = create_matrix(len(colored_image), len(colored_image[0]))
    for row_index in range(len(colored_image)):
        for pixel_index in range(len(colored_image[0])):
            red = 0.299 * colored_image[row_index][pixel_index][0]
            green = 0.587 * colored_image[row_index][pixel_index][1]
            blue = 0.114 * colored_image[row_index][pixel_index][2]
            matrix[row_index][pixel_index] = round(red + green + blue)
    return matrix
# ----greyscale function----


def blur_kernel(size):
    if size < 0:
        size = size*(-1)
    kernel = create_matrix(size,size)
    for rows_index in range(size):
        for cell_index in range(size):
            kernel[rows_index][cell_index] = 1/(size*size)
    return kernel


def apply_kernel(image, kernel):
    blur_image = create_matrix(len(image), len(image[0]))
    for row_index in range(len(image)):
        for pixel_index in range(len(image[0])):
            pixel = blurred_matrix(image_copy(len(kernel), image, row_index, pixel_index), kernel)
            blur_image[row_index][pixel_index] = pixel
    return blur_image


# creates a matrix with the appropriate pixels from image with the same size as the kernel
def image_copy(matrix_size, image, row_index, column_index):
    image_matrix = create_matrix(matrix_size, matrix_size)
    half_size = math.floor(matrix_size/2)
    for x in range(matrix_size):
        for y in range(matrix_size):
            if not_in_bounds(column_index+y-half_size, row_index+x-half_size, image):
                image_matrix[x][y] = image[row_index][column_index]
                continue
            image_matrix[x][y] = image[row_index+x-half_size][column_index+y-half_size]
    return image_matrix


# this function returns the blurred value of the center pixel of image_matrix
def blurred_matrix(image_matrix, kernel):
    blur_value = 0
    for row_index in range(len(kernel)):
        for pixel_index in range(len(kernel[0])):
            blur_value += image_matrix[row_index][pixel_index]*kernel[row_index][pixel_index]
    blur_too_big_v_too_small(blur_value)
    return round(blur_value)


# checks if some of the kernels goes out of the image bounds
def not_in_bounds(column_index, row_index, image):
    return column_index < 0 or column_index >= len(image[0]) or row_index < 0 or row_index >= len(image)


# checks that the blur value isn't to small or big.
def blur_too_big_v_too_small(blur_value):
    if blur_value > 255:
        return 255
    elif blur_value < 0:
        return 0
    else:
        return blur_value
# ----blur effect----


def bilinear_interpolation(image, y, x):
    if y%1 == 0 and x%1 == 0:
        return image[int(y)][int(x)]
    return round(if_xy_fractions(image, y, x))


def if_xy_fractions(image, y, x):
    back_x = math.floor(x)
    front_x = math.ceil(x)
    back_y = math.floor(y)
    front_y = math.ceil(y)
    x_minus = front_x - x
    y_minus = front_y - y
    x_0 = x - back_x
    y_0 = y - back_y
    return_value = 0
    if back_y != front_y and back_x != front_x:
        return_value = (image[back_y][back_x]*y_minus*x_0) +\
                       (image[front_y][back_x]*y_0*x_0) + \
                       (image[back_y][front_x]*y_minus*x_minus) + \
                   image[front_y][front_x]*y_0*x_minus
    elif back_y == front_y:
        return_value = (image[int(y)][back_x]*x_minus) + (image[int(y)][front_x]*x_0)
    elif front_x == back_x:
        return_value = (image[back_y][int(x)]*y_minus) + (image[front_y][int(x)]*y_0)
    return return_value
# ----bilinear interpolation----


def resize(image, new_height, new_width):
    matrix = create_matrix(new_height, new_width)
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            matrix[row_index][column_index] = bilinear_interpolation(image, row_index*(len(image)/new_height),
                                                                     column_index*(len(image[0])/new_width))
    matrix = corner_mapping(matrix, image)
    return matrix


def corner_mapping(matrix, image):
    matrix[0][0] = image[0][0]
    matrix[0][len(matrix[0]) - 1] = image[0][len(image[0]) - 1]
    matrix[len(matrix) - 1][0] = image[len(image) - 1][0]
    matrix[len(matrix)-1][len(matrix[0])-1] = image[len(image)-1][len(image[0])-1]
    return matrix


def rotate_90(image, direction):
    if direction == "R":
        return image_rotater_right(len(image), len(image[0]), image)
    elif direction == "L":
        return image_rotater_left(len(image), len(image[0]), image)


def image_rotater_right(rows, columns, image):
    matrix = create_matrix(columns, rows)
    for row_index in range(columns):
        for column_index in range(rows):
            matrix[row_index][column_index] = image[rows - 1 - column_index][row_index]
    return matrix


def image_rotater_left(rows, columns, image):
    matrix = create_matrix(columns, rows)
    for row_index in range(columns):
        for column_index in range(rows):
            matrix[row_index][column_index] = image[column_index][row_index]
    return matrix
# ----roatater----


def get_edges(image, blur_size, block_size, c):
    blur_matrix = blur_kernel(blur_size)
    blurred_image = apply_kernel(image, blur_matrix)
    r = block_size//2
    threshold = threshold_builder(blurred_image, r, blur_size)
    new_image = create_matrix(len(blurred_image), len(blurred_image[0]))
    for row_index in range(len(blurred_image)):
        for colmun_index in range(len(blurred_image[0])):
            if image[row_index][colmun_index] < threshold[row_index][colmun_index] - c:
                new_image[row_index][colmun_index] = 0
            else:
                new_image[row_index][colmun_index] = 255
    return new_image


def threshold_builder(blurred_image, r, blur_size):
    threshold = create_matrix(len(blurred_image), len(blurred_image[0]))
    for i in range(len(blurred_image)):
        for j in range(len(blurred_image[0])):
            threshold[i][j] = (avg(i, j, r, blurred_image, blurred_image[i][j], blur_size))
    return threshold


def avg(i, j, r, image, center_value, blur_size):
    sum = 0
    kernel_size = 0
    for row in range(i-r, i+r+1):
        for num in range(j-r, j+r+1):
            kernel_size += 1
            if not_in_bounds(num, row, image):
                sum += center_value
            else:
                sum += image[row][num]
    average = sum/(kernel_size)
    return average
# ----get edges----


def quantize(image, N):
    qimage = create_matrix(len(image), len(image[0]))
    for row_index in range(len(image)):
        for column_index in range(len(image[0])):
            qimage[row_index][column_index] = round(math.floor(image[row_index][column_index]*(N/255))*(255/N))
    return qimage
# ----quantize----


def quantize_colored_image(image, N):
    channels = separate_channels(image)
    for channel_index in range(len(channels)):
        channels[channel_index] = quantize(channels[channel_index],N)
    return combine_channels(channels)
# ----quantize_colored_image----


def add_mask(image1, image2, mask):
    new_image = create_matrix(len(mask), len(mask[0]))
    if type(image1[0][0]) == int and type(image2[0][0]) == int:
        real_mask = maskify(mask)
        for row_index in range(len(mask)):
            for column_index in range(len(mask[0])):
                new_image[row_index][column_index] = mask_formula(image1[row_index][column_index],
                                                                  image2[row_index][column_index],
                                                                  real_mask[row_index][column_index])
    elif type(image1[0][0]) != int and type(image2[0][0]) == int:
        new_image1 = separate_channels(image1)
        for index in range(len(new_image1)):
            new_image1[index] = add_mask(new_image1[index], image2, mask)
        new_image = combine_channels(new_image1)
    elif type(image1[0][0]) == int and type(image2[0][0]) != int:
        new_image2 = separate_channels(image2)
        for index in range(len(new_image2)):
            new_image2[index] = add_mask(new_image2[index], image2, mask)
        new_image = combine_channels(new_image2)
    elif type(image1[0][0]) != int and type(image2[0][0]) != int:
        new_image1 = separate_channels(image1)
        new_image2 = separate_channels(image2)
        for index in range(len(new_image1)):
            new_image = add_mask(new_image1, new_image2, mask)
    return new_image


def mask_formula(image1, image2, mask):
    return round(image1*mask + image2*(1-mask))


def maskify(image):
    if check_mask_is_10(image):
        return image
    else:
        mask = create_matrix(len(image), len(image[0]))
        for row_index in range(len(image)):
            for pixel_index in range(len(image[0])):
                mask[row_index][pixel_index] = round(image[row_index][pixel_index]/255)
        return mask


def check_mask_is_10(image):
    for row in image:
        for pixel in image[0]:
            if pixel < 0 or pixel > 1:
                return False
    return True
# ----add_mask----


def cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades):
    new_channels = quantize_colored_image(image, quant_num_shades)
    edges = get_edges(RGB2grayscale(image), th_block_size, blur_size, th_c)
    return add_mask(new_channels, edges, edges)



if __name__ == "__main__":
    loadout = str(sys.argv[1])
    saveout = str(sys.argv[2])
    image = ex5_helper.load_image(loadout)
    max_size = int(sys.argv[3])
    blur_size = int(sys.argv[4])
    block_size = int(sys.argv[5])
    c = int(sys.argv[6])
    num_of_shades = int(sys.argv[7])
    if len(sys.argv) != 8:
        print("wrong number of inputs")
        exit()
    if len(image) > len(image[0]) or len(image[0]) > max_size:
        resize(image, len(image)*(len(image[0]/max_size)),max_size)
    image = cartoonify(image, blur_size,block_size,c,num_of_shades)
    ex5_helper.save_image(image, saveout)


# image = ex5_helper.load_image("small_picture.jpg")
# matrix = separate_channels(image)
# matrix = matrix[0]
# ex5_helper.save_image(image, "G:\My Drive\CS\Pycharm Projects\ex5\\" + "vvvvv.jpg")
# test_image = combine_channels([[[1]],[[1]]])
# ex5_helper.save_image(channels, "G:\My Drive\CS\Pycharm Projects\ex5\\" + "aaaa.jpg")
# test_image = cartoonify(image, 5,5,5,10)
# ex5_helper.save_image(test_image, "G:\My Drive\CS\Pycharm Projects\ex5\\" + "abcd.jpg")
# # ex5_helper.show_image(channels)
# print(test_image)















