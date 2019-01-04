import tensorflow as tf
import glob
import matplotlib.image as img
import cv2
import matplotlib.pylab as plt
image_path = "/media/ubuntu/data/ADAS/Driver/object_detection/outimages"
sess = tf.InteractiveSession()
images = glob.glob(image_path + "/*.jpg")

for image in images:
    img = cv2.imread(image)
    flipimg = tf.image.flip_left_right(img)
    flip_img = tf.cast(flipimg, tf.uint8)
    cv2.imshow("pre_image",img)
    cv2.imshow("flip_img",sess.run(flip_img))
    cv2.waitKey(1)
cv2.destroyAllWindows()
