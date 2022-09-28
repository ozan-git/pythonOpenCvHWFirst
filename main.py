import cv2.cv2 as cv2
import numpy as np


# 1) The user is asked to write the file path of the image he wants to process.
#
# 2) The size information of the image is saved in the predetermined "row_image" (row) and "column_image" variables.
#
# 3) a function checks if the image is grayscale or RGB and if it is grayscale the "image_gray_scale" variable is
# false if not true.
#
# 4) The values that the user wants to divide the photo into parcels according to the "block_vertical"
# and "block_horizontal" values are taken from the user. The vertical length value to the "block_vertical"
# variable is assigned the horizontal length value to the "block_horizontal" variable. These values are assigned
# to the "block_dim_tuple" variable.
#
# 5) The visual is zoned according to the "block_dim_tuple" values. Each zone is averaged according to the intensity
# level of the colors there and is zoned to be the color of the average intensity level. If it is RGB, RGB color levels
# are not used, otherwise it is colored according to grayscale.
#
# 6) the new image output is saved to the specified file path.

def main():
    # 1)
    file_path = input("Please enter the file path of the image you want to process: ")
    # 2)
    image = cv2.imread(file_path)
    row_image, col_image = image.shape[:2]
    # print image row count and column count
    print("Image row count: ", row_image)
    print("Image column count: ", col_image)
    # 3)
    image_gray_scale = False
    if len(image.shape) == 2:
        image_gray_scale = True
    # 4)
    block_vertical = int(input("Please enter the number of blocks vertically: "))
    hor_block = int(input("Please enter the number of blocks horizontally: "))
    block_dim_tuple = (block_vertical, hor_block)
    # 5)
    new_image = np.zeros((row_image, col_image, 3), np.uint8)
    for i in range(block_vertical):
        for j in range(hor_block):
            block = image[int(i * row_image / block_vertical):int((i + 1) * row_image / block_vertical),
                    int(j * col_image / hor_block):int((j + 1) * col_image / hor_block)]
            if image_gray_scale:
                new_image[int(i * row_image / block_vertical):int((i + 1) * row_image / block_vertical),
                int(j * col_image / hor_block):int((j + 1) * col_image / hor_block)] = np.mean(block)
            else:
                new_image[int(i * row_image / block_vertical):int((i + 1) * row_image / block_vertical),
                int(j * col_image / hor_block):int((j + 1) * col_image / hor_block)] = \
                    np.mean(block, axis=(0, 1))
    # 6)
    cv2.imwrite("new_image.jpg", new_image)


if __name__ == "__main__":
    main()
