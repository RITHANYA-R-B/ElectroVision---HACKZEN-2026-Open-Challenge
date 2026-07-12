from ultralytics import YOLO
from collections import defaultdict

# Load trained model
model = YOLO("best.pt")


def detect(image_path):
    """
    Detect electronic components in a PCB image.

    Returns:
        processed_image : Image with bounding boxes
        detected_components : List containing
            Component name
            Count
            Average confidence
    """

    results = model(image_path)

    # Image with bounding boxes
    processed_image = results[0].plot()

    component_data = defaultdict(lambda: {
        "Count": 0,
        "Confidence Sum": 0
    })

    # Process detections
    for box in results[0].boxes:

        cls = int(box.cls)
        confidence = float(box.conf) * 100

        component_name = model.names[cls]

        component_data[component_name]["Count"] += 1
        component_data[component_name]["Confidence Sum"] += confidence

    detected_components = []

    for component, values in component_data.items():

        average_confidence = round(
            values["Confidence Sum"] / values["Count"],
            2
        )

        detected_components.append({
            "Component": component,
            "Count": values["Count"],
            "Confidence": average_confidence
        })

    return processed_image, detected_components