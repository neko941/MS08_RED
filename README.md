# gen_rectangle_mask.py  
> Generate random rectangle mask with given angle (default = 0)

```
!python gen_rectangle_mask.py -d <image_directory> -r <mask_to_image_ratio> -a <rotation_angle> -z
```

Optional arguments:
```
  -h, --help       show this help message and exit
  -d , --img_dir   Input ground truth images folder
  -r , --ratio     Input ratio mask to image (0.4 = 40%)
  -a , --angle     Input angle
  -z, --zip        Zip and delete masks folder
```

Example
```
gen_rectangle_mask.py -d "images" -r 0.04 -z
gen_rectangle_mask.py -d "images" -r 0.04 -a 45 -z
gen_rectangle_mask.py -d "images" -r 0.04 -a 90 -z
gen_rectangle_mask.py -d "images" -r 0.04 -a 135 -z
gen_rectangle_mask.py -d "images" -r 0.1 -z
gen_rectangle_mask.py -d "images" -r 0.1 -a 45 -z
gen_rectangle_mask.py -d "images" -r 0.1 -a 90 -z
gen_rectangle_mask.py -d "images" -r 0.1 -a 135 -z
gen_rectangle_mask.py -d "images" -r 0.2 -z
gen_rectangle_mask.py -d "images" -r 0.2 -a 45 -z
gen_rectangle_mask.py -d "images" -r 0.2 -a 90 -z
gen_rectangle_mask.py -d "images" -r 0.2 -a 135 -z
gen_rectangle_mask.py -d "images" -r 0.25 -z
gen_rectangle_mask.py -d "images" -r 0.25 -a 45 -z
gen_rectangle_mask.py -d "images" -r 0.25 -a 90 -z
gen_rectangle_mask.py -d "images" -r 0.25 -a 135 -z
```

# gen_one_centered_rectangle_mask.py  
> Generate one centered rectangle mask with given angle (default = 0)
```
!python gen_one_centered_rectangle_mask.py -d <image_directory> -r <mask_to_image_ratio> -a <rotation_angle> -z
```

Optional arguments:
```
  -h, --help       show this help message and exit
  -d , --img_dir   Input ground truth images folder
  -r , --ratio     Input ratio mask to image (0.4 = 40%)
  -a , --angle     Input angle
  -z, --zip        Zip and delete masks folder
```

Example
```
gen_one_centered_rectangle_mask.py -d "images" -r 0.04 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.04 -a 45 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.04 -a 90 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.04 -a 135 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.1 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.1 -a 45 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.1 -a 90 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.1 -a 135 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.2 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.2 -a 45 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.2 -a 90 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.2 -a 135 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.25 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.25 -a 45 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.25 -a 90 -z
gen_one_centered_rectangle_mask.py -d "images" -r 0.25 -a 135 -z
```
