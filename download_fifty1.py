import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    "open-images-v6", 
    "train", 
    label_types=["detections", "classifications"], 
    classes = ["Traffic light"],
    max_samples=1000,
    seed=51,
    shuffle=True
)

session = fo.launch_app(dataset)

session.wait()

export_dir = "/Users/hairanliang/Downloads/DSU_Object_Detection/traffic_lights_train"
dataset.export(
    export_dir=export_dir,
    dataset_type=fo.types.COCODetectionDataset,
    label_field="detections",
)

session.wait()