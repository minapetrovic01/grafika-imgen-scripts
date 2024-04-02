import cv2
import numpy as np

def create_four_images(input_image, permutation):
    partitions = np.array_split(input_image, 4, axis=0)
    partitions = [np.array_split(part, 4, axis=1) for part in partitions]

    enumerated_partitions = [ partitions[i][j] for i in range(4) for j in range(4)]
    print(np.shape(enumerated_partitions))

    enumerated_partitions_permuted = [enumerated_partitions[i] for i in permutation]

    new_image = np.zeros_like(input_image)

    for i, partition in enumerate(enumerated_partitions_permuted):
        row = i // 4
        col = i % 4
        y_start = row * (input_image.shape[0] // 4)
        y_end = (row + 1) * (input_image.shape[0] // 4)
        x_start = col * (input_image.shape[1] // 4)
        x_end = (col + 1) * (input_image.shape[1] // 4)
        new_image[y_start:y_end, x_start:x_end] = partition

    return new_image

input_image = cv2.imread('2k_mars.jpg')

# permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
# permutation = [15, 12, 13, 14, 3,0,1,2,7,4,5,6,11,8,9,10]  
# permutation = [ 13, 14,15, 12, 1,2,3,0,5,6,7,4,9,10,11,8]
# permutation = [ 7,4,5,6,11,8,9,10,15,12,13,14,3,0,1,2]
permutation=[5,6,7,4,9,10,11,8,13,14,15,12,1,2,3,0]

output_image = create_four_images(input_image, permutation)

cv2.imwrite('output_image22.jpg', output_image)
