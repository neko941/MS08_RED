import argparse
import cv2
import os
from alive_progress import alive_bar
import shutil
import random
import numpy as np

def check_image_shape(path):
	shape = []
	num = 0

	for root, directories, files in os.walk(path):
		for file in files: 
			im = cv2.imread(os.path.join(root, file))

			num += 1

			if im.shape not in shape:
				shape.append(im.shape)
	return shape, num

def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)

    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH))

def generate_rectangle(size, mask_to_image, angel):
	mask_width_ratio = random.uniform(mask_to_image, 1)
	mask_height_ratio = mask_to_image / mask_width_ratio
	mask_height = round(size[0] * mask_height_ratio)
	mask_width = round(size[1] * mask_width_ratio)

	rectangle = np.zeros((mask_width, mask_height, 3), np.uint8)
	rectangle.fill(255)

	rectangle = rotate_bound(rectangle, angel)
	return rectangle

def generate_rec_mask(size, num_images, path, mask_to_image, angle):
	if os.path.exists("masks"):
		shutil.rmtree("masks")
	os.makedirs("masks")

	with alive_bar(num_images) as bar:
		for root, directories, files in os.walk(path):
			for file in files:
				rectangle = generate_rectangle(size, mask_to_image, angle)

				while (rectangle.shape[0] > size[0]) or (rectangle.shape[1] > size[1]):
					rectangle = generate_rectangle(size, mask_to_image, angle)

				mask = np.zeros((size[1], size[0], 3), np.uint8)
				position_height = random.randint(0, size[0] - rectangle.shape[0])
				position_width = random.randint(0, size[1] - rectangle.shape[1])
				mask[position_height:(position_height+rectangle.shape[0]), position_width:(position_width+rectangle.shape[1])] = rectangle
				cv2.imwrite(f"masks/{file}", mask)

				bar()

def zip_directory(size, num_images, mask_to_image, angle):
	if angle == 0:
		shutil.make_archive(f"mask-rectangle_{int(mask_to_image*100)}%_{num_images}_{size[0]}x{size[1]}", "zip", base_dir="masks")
	else:
		shutil.make_archive(f"mask-rectangle_{int(mask_to_image*100)}%_{num_images}_{size[0]}x{size[1]}_r{angle}", "zip", base_dir="masks")
	shutil.rmtree("masks")

def take_arguments():
	parser = argparse.ArgumentParser(description="Generate Random Rectangle Mask")
	parser.add_argument("-d", "--img_dir", type=str, metavar="", required=True, help="Input ground truth images folder")
	parser.add_argument("-r", "--ratio", type=float, metavar="", default=0.1 , help="Input ratio mask to image (0.4 = 40%)")
	parser.add_argument("-a", "--angle", type=int, metavar="", default=0 , help="Input angle")
	parser.add_argument("-z", "--zip", action="store_true", help="Zip and delete masks folder")
	return parser.parse_args()


if __name__ == "__main__":
	args = take_arguments()

	shape, num_images = check_image_shape(args.img_dir)

	# if the folder has an image with different size compared to others in the folder, break the program
	assert len(shape) == 1

	generate_rec_mask(shape[0], num_images, args.img_dir, args.ratio, args.angle)
	if args.zip:
		zip_directory(shape[0], num_images, args.ratio, args.angle)
