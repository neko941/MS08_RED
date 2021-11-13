import sys
import cv2
from skimage.metrics import structural_similarity as SSIM
from skimage.metrics import mean_squared_error as MSE
from skimage.metrics import peak_signal_noise_ratio as PSNR
import numpy as np

image = cv2.imread(sys.argv[1])      
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

result = cv2.imread(sys.argv[2])      
result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)


mae = (np.abs(np.subtract(image, result))).mean()
print("Mean Absolute Error (MAE): ", mae)

mqe = MSE(image, result)
print("Mean Square Error (MSE): ", mqe)

psnr = PSNR(image, result)
print("Peak Signal to Noise Ratio (PSNR): ", psnr)

ssim = SSIM(image, result, multichannel=True)
print("Structure Similarity Index Measure (SSIM): ", ssim)