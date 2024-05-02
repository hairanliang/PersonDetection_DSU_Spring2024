"""
Python script that performs real-time detection using YOLOv8
"""

from ultralytics import YOLO
from ultralytics.models.yolo.segment import SegmentationPredictor

import cv2

model = YOLO("yolov8n-seg.pt")

results = model.predict(source="0", show=True)

print(results)