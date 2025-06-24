from ultralytics import YOLO
import cv2

# Load model
model = YOLO('yolov8n.pt')  # Use YOLOv8 nano for lightweight

# Classes of interest: person=0, cat=15, dog=16
INTERESTED_CLASSES = [0, 15, 16]


def detect_living_beings(image_path):
    results = model(image_path)[0]
    counts = {'person': 0, 'cat': 0, 'dog': 0}
    img = cv2.imread(image_path)

    for box in results.boxes:
        cls_id = int(box.cls[0])
        if cls_id in INTERESTED_CLASSES:
            label = model.names[cls_id]
            counts[label] += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    output_path = f'static/results/output.jpg'
    cv2.imwrite(output_path, img)
    return counts, output_path
