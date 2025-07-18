import cv2
import numpy as np

def detect_lines(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=80, minLineLength=50, maxLineGap=10)

    features = {
        'line_count': len(lines) if lines is not None else 0,
        'lines_detected': bool(lines is not None)
    }
    return features