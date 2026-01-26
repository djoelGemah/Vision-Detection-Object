import os
import random
import shutil

# ===== KONFIGURASI =====
SOURCE_DIR = "raw_dataset"
DEST_DIR = "dataset"
TRAIN_RATIO = 0.8   # 80% train, 20% val
IMAGE_EXTENSIONS = (".jpg", ".png", ".jpeg")

# ======================

src_images = os.path.join(SOURCE_DIR, "images")
src_labels = os.path.join(SOURCE_DIR, "labels")

dst_img_train = os.path.join(DEST_DIR, "images", "train")
dst_img_val   = os.path.join(DEST_DIR, "images", "val")
dst_lbl_train = os.path.join(DEST_DIR, "labels", "train")
dst_lbl_val   = os.path.join(DEST_DIR, "labels", "val")

# Ambil semua gambar
images = [f for f in os.listdir(src_images) if f.lower().endswith(IMAGE_EXTENSIONS)]

print(f"Total gambar ditemukan: {len(images)}") 

# Shuffle supaya random
random.shuffle(images)

# Split
split_idx = int(len(images) * TRAIN_RATIO)
train_images = images[:split_idx]
val_images = images[split_idx:]

def copy_pair(img_name, img_dst, lbl_dst):
    img_src_path = os.path.join(src_images, img_name)
    lbl_name = os.path.splitext(img_name)[0] + ".txt"
    lbl_src_path = os.path.join(src_labels, lbl_name)

    if not os.path.exists(lbl_src_path):
        print(f"⚠️ Label tidak ditemukan untuk {img_name}, dilewati")
        return

    shutil.copy(img_src_path, img_dst)
    shutil.copy(lbl_src_path, lbl_dst)

# Copy train
for img in train_images:
    copy_pair(img, dst_img_train, dst_lbl_train)

# Copy val
for img in val_images:
    copy_pair(img, dst_img_val, dst_lbl_val)

print("✅ Split dataset selesai")
print(f"Train: {len(train_images)} gambar")
print(f"Val  : {len(val_images)} gambar")
