import cv2.cv2 as cv2
import numpy as np


# 1) The user is asked to write the file path of the image he wants to process.
# 2) The size information of the image is saved in the predetermined "row_image" (row) and "column_image" variables.
# 3) a function checks if the image is grayscale or RGB and if it is grayscale the "image_gray_scale"
# variable is false if not true. print image is grayscale or RGB is printed.
# 4) The values that the user wants to divide the photo into parcels according to the "block_vertical"
# "block_horizontal" values are taken from the user. The vertical length value to the "block_vertical"
# variable is assigned the horizontal length value to the "block_horizontal" variable. These values
# are assigned to the "block_dim_tuple" variable.
# 5) The image is zoned according to the "block_dim_tuple" values. Each region is zoned so that the
# average of the colors there is in its color.
# 6) the new image output is saved to the specified file path.


def main():
    # 1) The user is asked to write the file path of the image he wants to process.
    file_path = input("Please enter the path of the image you want to process: ")
    # 2) The size information of the image is saved in the predetermined "row_image" (row) and "column_image" variables.
    row_image, column_image = cv2.imread(file_path).shape[:2]
    # 3) a function checks if the image is grayscale or RGB and if it is grayscale the "image_gray_scale"
    # variable is false if not true. print image is grayscale or RGB is printed.
    image_gray_scale = check_image_gray_scale(file_path)
    if image_gray_scale:
        print("Image is grayscale.")
    else:
        print("Image is RGB.")
    # 4) The values that the user wants to divide the photo into parcels according to the "block_vertical"
    # "block_horizontal" values are taken from the user. The vertical length value to the "block_vertical"
    # variable is assigned the horizontal length value to the "block_horizontal" variable. These values
    # are assigned to the "block_dim_tuple" variable.
    block_vertical = int(input("Please enter the vertical length value: "))
    block_horizontal = int(input("Please enter the horizontal length value: "))
    block_dim_tuple = (block_vertical, block_horizontal)
    # 5) The image is zoned according to the "block_dim_tuple" values. Each region is zoned so that the
    # average of the colors there is in its color.
    average_color_image_val = average_color_image(file_path, block_dim_tuple, row_image, column_image)
    # 6) the new image output is saved to the specified file path.
    output_file_path = input("Please enter the path of the image you want to save: ")
    cv2.imwrite(output_file_path, average_color_image_val)


def check_image_gray_scale(file_path):
    image = cv2.imread(file_path)
    if len(image.shape) == 2:
        return True
    else:
        return False


def average_color_image(file_path, block_dim_tuple, row_image, column_image):
    image = cv2.imread(file_path)
    average_color_image_val = np.zeros((row_image, column_image, 3), np.uint8)
    for i in range(0, row_image, block_dim_tuple[0]):
        for j in range(0, column_image, block_dim_tuple[1]):
            average_color_image[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]] = np.mean(
                image[i:i + block_dim_tuple[0], j:j + block_dim_tuple[1]], axis=(0, 1))
    return average_color_image_val


if __name__ == '__main__':
    main()