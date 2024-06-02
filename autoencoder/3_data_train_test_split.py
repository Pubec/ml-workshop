import os
import shutil
import random

# Set the seed for reproducibility
random.seed(42)

# Define the paths
images_folder = "148color.images"
train_folder = "148color.train"
test_folder = "148color.test"

os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

files = os.listdir(images_folder)
files.sort()

file_pairs = []
for i in range(0, len(files), 2):
    file_pairs.append((files[i], files[i + 1]))

random.shuffle(file_pairs)
split_index = int(0.8 * len(file_pairs))
train_pairs = file_pairs[:split_index]
test_pairs = file_pairs[split_index:]


def copy_files(pairs, destination_folder):
    for input_file, label_file in pairs:
        shutil.copy(
            os.path.join(images_folder, input_file),
            os.path.join(destination_folder, input_file),
        )
        shutil.copy(
            os.path.join(images_folder, label_file),
            os.path.join(destination_folder, label_file),
        )


copy_files(train_pairs, train_folder)
copy_files(test_pairs, test_folder)

print(f"Training set size: {len(train_pairs)}")
print(f"Testing set size: {len(test_pairs)}")
