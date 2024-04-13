import cv2 # OpenCV
import random # Random

img = cv2.imread('png test-assets/sponge.jpg', 1) # reading sponge.jpg in grayscale 
# NOTE: CV2 READS COLOR IMAGES IN BGR CHANNEL ORDER
# THE FOLLOWING ARE ALL IMREAD MODES
# -1 : cv2.IMREAD_COLOR : loads color, transparency of image neglected, default flag
#  0 : cv2.IMREAD_GRAYSCALE : loads grayscale
#  1 : cv2.IMREAD_UNCHANGED : loads as entire, including alpha channel

img = cv2.resize(img, (400, 400)) # resize image, stretches aspect
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # resize image by some multiplier (must set (0, 0) as second param)

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # second parameter has certain constants? check documentation to do other rotations


cv2.imwrite('png test-assets/new_sponge.jpg', img) # write file into given directory

cv2.imshow('Sponge', img)
cv2.waitKey(0) # wait INFINITE, not 0 time for some input. Any number greater is n-MILLIseconds
cv2.destroyAllWindows() # proceeds to delete windows

sponge = img.copy() # copying img to new array sponge

print(img) # prints numpy array of RGB values
print(type(img)) # shows that img's type is a numpy.ndarray
print(img.shape) # uses numpy to tell you the height x width x channel
# NOTE: channels count is not a quantity of a grayscale image, grayscales only have height x width
# NOTE: REMINDER AGAIN, cv2 reads it as BGR, not RGB
# to better visualize how numpy represents images, think of a 2D table full of BGR values in tuples
print(img[0, 0]) # prints the BGR tuple value of the very top-left pixel
print(img[199][50:200]) # prints a slice of the 50th to 199th pixels in the last row. the image is 200 x 200
# NOTE: arrays 0-indexed, and slices are [inclusive:exclusive]

# the following loops through the pixel by row then column, and sets it to random value 
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# display the new image of spongebob in a colorful oblivion
cv2.imshow('hh', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


bob = sponge[75:125, 60:137]
sponge[10:60, 60:137] = bob

cv2.imshow('bob', sponge)
cv2.waitKey(0)
cv2.destroyAllWindows()
