import cv2
from skimage.metrics import structural_similarity as SSIM
from skimage.metrics import mean_squared_error as MSE
from skimage.metrics import peak_signal_noise_ratio as PSNR
import numpy as np
import os
from alive_progress import alive_bar

MAEs = []
MQEs = []
PSNRs = []
SSIMs = []


'''
@author: Nguyen Khoa
'''

def evaluate(input_path, output_path):
    '''
    function to evalute metrics of image inpainting
    :parameters
    input_path: path to test folders image
    output_path: path to test output image

    return : MAE, MQE, PSNR, SSIM values
    '''
    with alive_bar(1000) as bar:
        for root, directories, files in os.walk(input_path):
            for file in files:
                print(file)

                image = cv2.imread(os.path.join(input_path, file))      
                image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

                result = cv2.imread(os.path.join(output_path, file))      
                result = cv2.cvtColor(result,cv2.COLOR_BGR2RGB)

                mae = (np.abs(np.subtract(image, result))).mean()
                MAEs.append(mae)

                mqe = MSE(image, result)
                MQEs.append(mqe)

                psnr = PSNR(image, result)
                PSNRs.append(psnr)

                ssim = SSIM(image, result, multichannel=True)
                SSIMs.append(ssim)

                bar()
 
    print("Average MAE: {:.4f}".format(sum(MAEs) / len(MAEs)))
    print("Average MSE: {:.4f}".format(sum(MQEs) / len(MQEs)))
    print("Average PSNR: {:.4f}".format(sum(PSNRs) / len(PSNRs)))
    print("Average SSIM: {:.4f}".format(sum(SSIMs) / len(SSIMs)))

if __name__ == "__main__":
    evaluate("Test/Inputs/images", "Test/Outputs/")