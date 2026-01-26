import cv2
from ultralytics import YOLO
from datetime import datetime
import os
import time
from collections import Counter

# =========================
# PATH KONFIGURASI
# =========================
MODEL_PATH = r"D:\deteksi\best.pt"
SAVE_DIR = r"D:\deteksi\rekap_penjualan"
NOTE_PATH = os.path.join(SAVE_DIR, "penjualan.txt")

os.makedirs(SAVE_DIR, exist_ok=True)

# =========================
# DAFTAR HARGA PRODUK
# =========================
HARGA_PRODUK = {
    "ceres": 32000,
    "parfume": 18000
}

# =========================
# LOAD MODEL YOLOv8
# =========================
model = YOLO(MODEL_PATH)

# =========================
# AKTIFKAN KAMERA
# =========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera tidak bisa dibuka")
    exit()

print("📸 Pastikan kotak deteksi muncul")
print("👉 Tekan 's' untuk simpan transaksi")
print("👉 Tekan 'q' untuk keluar")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # =========================
    # DETEKSI REALTIME
    # =========================
    results = model(frame, conf=0.5, verbose=False)
    annotated_frame = frame.copy()
    detected_objects = []

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        label = results[0].names[cls_id]
        conf = float(box.conf[0])

        detected_objects.append(label)

        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            annotated_frame,
            f"{label} {conf:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # =========================
    # STATUS DI LAYAR
    # =========================
    if detected_objects:
        status_text = "OBJEK TERDETEKSI - AMAN - Pencet [S]"
        color = (0, 255, 0)
    else:
        status_text = "TIDAK ADA OBJEK - JANGAN SIMPAN"
        color = (0, 0, 255)

    cv2.putText(
        annotated_frame,
        status_text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.imshow("Deteksi Produk", annotated_frame)
    key = cv2.waitKey(1) & 0xFF

    # =========================
    # SIMPAN TRANSAKSI
    # =========================
    if key == ord('s'):

        if not detected_objects:
            print("⚠️ Tidak ada produk terdeteksi, transaksi dibatalkan.")
            continue

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # FOTO PRODUK
        produk_path = os.path.join(
            SAVE_DIR, f"produk_{timestamp}.jpg"
        )
        cv2.imwrite(produk_path, frame)

        # HITUNG QTY & TOTAL
        counter = Counter(detected_objects)
        total_harga = 0

        # CATAT KE FILE
        with open(NOTE_PATH, "a", encoding="utf-8") as f:
            f.write("\n" + "=" * 45 + "\n")
            f.write(f"Waktu Transaksi : {datetime.now()}\n")
            f.write(f"Foto Produk    : {os.path.basename(produk_path)}\n")
            f.write("Detail Produk:\n")

            for produk, qty in counter.items():
                harga = HARGA_PRODUK.get(produk, 0)
                subtotal = harga * qty
                total_harga += subtotal

                f.write(
                    f"- {produk} | {qty} x {harga} = {subtotal}\n"
                )

            f.write(f"TOTAL HARGA : {total_harga}\n")

        print("✅ Produk & harga tersimpan")

        # =========================
        # FOTO PEMBELI
        # =========================
        print("📷 Ambil foto pembeli...")
        time.sleep(5)

        ret, frame = cap.read()
        pembeli_path = os.path.join(
            SAVE_DIR, f"pembeli_{timestamp}.jpg"
        )
        cv2.imwrite(pembeli_path, frame)

        with open(NOTE_PATH, "a", encoding="utf-8") as f:
            f.write(
                f"Foto Pembeli  : {os.path.basename(pembeli_path)}\n"
            )

        print("✅ Transaksi selesai")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
