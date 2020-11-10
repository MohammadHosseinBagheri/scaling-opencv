# open cv library
import cv2


# method fucntion
def set_method(number):
    if number == 0:
        return cv2.INTER_NEAREST
    elif number == 1:
        return cv2.INTER_LINEAR
    elif number == 2:
        return cv2.INTER_AREA
    elif number == 3:
        return cv2.INTER_CUBIC
    else:
        return cv2.INTER_LANCZOS4


# read image
image = cv2.imread('./test.png')
# ----------------------------------
# scale inputs
print('----------------------------------')
scaleX = float(input("Enter Scale X : "))
scaleY = float(input('Enter Scale Y : '))
print('----------------------------------')
print("0-INTER_NEAREST")
print("1-INTER_LINEAR")
print("2-INTER_AREA")
print("3-INTER_CUBIC")
print("4-INTER_LANCZOS4")
method_number = int(input('Enter Number of Methods : '))
method = set_method(method_number)
# ----------------------------------

# scaling methods
resized_image = cv2.resize(image, None, fx=scaleX,
                           fy=scaleY, interpolation=method)
# ----------------------------------

# show image
cv2.imshow('imgae', resized_image)
# ----------------------------------

# exit key
exit_key = cv2.waitKey(0)
cv2.destroyAllWindows()
# ----------------------------------
