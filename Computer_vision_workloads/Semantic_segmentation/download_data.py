from datasets import load_dataset

DATASET_NAME = "scene_parse_150"

train_dataset = load_dataset(DATASET_NAME, split="train")
test_dataset = load_dataset(DATASET_NAME, split="test")
