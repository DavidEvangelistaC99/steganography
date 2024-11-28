"""
Cálculo de métricas de calidad en imágenes
INICTEL-2024
@david_evangelista
"""

# ------------------------------------------------------------------------------------------------------------------
# Librerías de esteganografía desarrolladas
# ------------------------------------------------------------------------------------------------------------------

import math
import cv2
import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable

# ------------------------------------------------------------------------------------------------------------------
# Variables y Funciones
# ------------------------------------------------------------------------------------------------------------------

def read_bmp(image_name):
	return cv2.imread(image_name)

# PSNR
def calculate_psnr(image_1,image_2):

	s = read_bmp(image_1)
	r = read_bmp(image_2)

	height, width, channel = s.shape
	size = height*width

	sb,sg,sr = cv2.split(s)
	rb,rg,rr = cv2.split(r)

	mseb = ((sb-rb)**2).sum()
	mseg = ((sg-rg)**2).sum()
	mser = ((sr-rr)**2).sum()

	MSE = (mseb+mseg+mser)/(3*size)
	psnr = 10*math.log10(255**2/MSE)

	return round(psnr,2)

# Default constants SSIM
# K = [0.01, 0.03]
# L = 255;
# window_size = 11

def calculate_ssim(image_1, image_2, K = [0.01, 0.03], window_size = 11, L = 255):

	# Opencv image load
	I1 = cv2.imread(image_1)
	I2 = cv2.imread(image_2)
	I2 = cv2.resize(I2, I1.shape[0:2])

	# Tensors
	I1 = torch.from_numpy(np.rollaxis(I1, 2)).float().unsqueeze(0) / 255.0
	I2 = torch.from_numpy(np.rollaxis(I2, 2)).float().unsqueeze(0) / 255.0

	# Tensor.autograd.Variable (Automatic differentiation variable)
	I1 = Variable(I1, requires_grad = True)
	I2 = Variable(I2, requires_grad = True)

	_, channel1, _, _ = I1.size()
	_, channel2, _, _ = I2.size()
	channel = min(channel1, channel2)

	# Gaussian window generation
	sigma = 1.5  # default
	gauss = torch.Tensor([math.exp(-(x - window_size // 2) ** 2 / float(2 * sigma ** 2)) for x in range(window_size)])
	_1D_window = (gauss / gauss.sum()).unsqueeze(1)
	_2D_window = _1D_window.mm(_1D_window.t()).float().unsqueeze(0).unsqueeze(0)
	window = Variable(_2D_window.expand(channel, 1, window_size, window_size).contiguous())

	C1 = K[0] ** 2;
	C2 = K[1] ** 2;

	mu1 = F.conv2d(I1, window, padding = window_size // 2, groups = channel)
	mu2 = F.conv2d(I2, window, padding = window_size // 2, groups = channel)

	mu1_sq = mu1.pow(2)
	mu2_sq = mu2.pow(2)
	mu1_mu2 = mu1 * mu2

	sigma1_sq = F.conv2d(I1 * I1, window, padding = window_size // 2, groups = channel) - mu1_sq
	sigma2_sq = F.conv2d(I2 * I2, window, padding = window_size // 2, groups = channel) - mu2_sq
	sigma12 = F.conv2d(I1 * I2, window, padding = window_size // 2, groups = channel) - mu1_mu2

	ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
	ssim_mean = ssim_map.mean()
	ssim_data = ssim_mean.data
	ssim_value = ssim_data.item()

	return round(ssim_value,12)