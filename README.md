# Steganography-Based Image Transmission over UHF Radio Links

<p align="center">
  <img src="images/system.png" width="900">
</p>

<p align="center">
  <em>End-to-end system for image steganography, transmission, and reception using New Packet Radio (NPR) modules over UHF links.</em>
</p>

## Overview

This repository contains data acquisition and image processing algorithms developed during my 2024 internship at INICTEL-UNI, within the areas of Digital Signal Processing, Image Processing, and Artificial Intelligence, with an emphasis on the secure transmission of images through radiofrequency communication systems.<br><br>
The project addresses the design, implementation, and evaluation of image steganography techniques aimed at hiding information within digital images, analyzing the effectiveness of hiding algorithms in both the spatial and frequency domains.
For the transmission of steganographic images, the system employs New Packet Radio (NPR) UHF communication modules, specifically designed to operate in UHF frequency bands.

## Methods

The project focuses on the design and implementation of steganography algorithms
using high-level programming languages, with an exploratory approach to data
hiding in images related to agricultural applications.

### Spatial-domain steganography
- Least Significant Bit (LSB)
- 2-LSB
- Edge-based methods (Canny)

### Frequency-domain steganography
- Chromatic subsampling
- Discrete Cosine Transform (DCT)
- Quantization

### Performance metrics
- Peak Signal-to-Noise Ratio (PSNR)
- Structural Similarity Index Measure (SSIM)

## Results

Experimental results were obtained using a reference 256×256 Lenna image and
a frequency-domain steganography-based compression scheme.

- Image transmission time: 2.49 s
- PSNR: 34.43 dB
- SSIM: 0.944

These results demonstrate an effective balance between transmission efficiency,
image quality, and robustness for secure wireless image communication.

## Repository Structure

- `docs/`: reviewed articles and technical references used during development
- `frequencySteganography/`: scripts for frequency-domain steganography
- `spatialSteganography/`: scripts for spatial-domain steganography
- `images/`: resulting images from spatial and frequency steganography
- `npr-main/`: scripts for image transmission and reception using NPR modules

## Hardware Setup

The project was developed and validated using the following hardware:

- UHF transmission modules (NPR)
- Two UHF antennas
- Ethernet connection cables
- Two Raspberry Pi 4 (hosts)
- Two laptops (hosts)

## Requirements

- Python 3.10+
- Pillow
- socket
- pickle
- NumPy
- Matplotlib

## Author

**David Fernando Evangelista Cuti**  
National University of Engineering (UNI), Peru

