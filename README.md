Pedestrian Anomaly Detection
Overview

This project implements a computer vision–based pedestrian anomaly detection system using frame-level video analysis, motion features, and object tracking. The backend integrates deep learning and classical vision techniques to identify abnormal pedestrian behavior in surveillance videos.

The system has been tested on the UCSD Pedestrian Dataset and supports automatic frame-to-video reconstruction for visual analysis of results.

Key Features

Detection of abnormal pedestrian activities

High-accuracy pedestrian tracking

Foreground mask generation for preprocessing

Optical flow–based motion feature extraction

Frame-based anomaly analysis

Automatic video generation from output frames

Modular and extensible pipeline

Technologies Used

Python

OpenCV

NumPy

Optical Flow

YOLO-based pedestrian tracking

Frame-based motion analysis

Dataset

This project uses the UCSD Pedestrian Dataset (Ped1).

Dataset download:

UCSD_Anomaly_Dataset.v1p2


Expected directory structure:

UCSD_Anomaly_Dataset/
└── UCSDped1/
    ├── Train/
    └── Test/


⚠️ The dataset is not included in this repository due to size constraints.

Project Structure
├── run.py               # Main pilot script
├── utils.py             # Dataset handling and test selection
├── test_script.py       # Loads pretrained features and processes test samples
├── frames2video.py      # Converts output frames into video
├── track.py             # Pedestrian tracking (restricted to class 'person')
├── bg.py                # Foreground mask generation
├── features/            # Pretrained feature data
├── output_folders/      # Generated output frames
└── output_without_tracking/  # Generated output videos

Installation

It is recommended to use Anaconda.

Create and activate an environment:

conda create -n anomaly python=3.9
conda activate anomaly


Install dependencies:

pip install -r requirements.txt

Usage

Run the main pipeline using:

python run.py


Optional arguments:

-test : Number of test samples to process (default = 36)

-tracking : Enable pedestrian tracking (default = true)

Output Examples

Foreground mask generation

Abnormal behavior detection

Pedestrian tracking visualization

Final reconstructed output videos

Output videos are saved automatically after frame processing.

Performance

The system demonstrates competitive performance on the UCSD Pedestrian dataset when compared with existing anomaly detection methods.

Method	ROC AUC
Proposed Method	0.91
Deep Ordinal Regression	0.92
Full-BVP	0.83
H-MDT CRF	0.82
Notes

OpenCV GUI functions are disabled for Windows compatibility

Frame ordering is handled numerically to ensure correct video reconstruction

Designed for extensibility and experimentation

License

This project is released for educational and research purposes.
You are free to use, modify, and extend it with proper attribution.
