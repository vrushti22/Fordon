import cv2
import numpy as np
import time

# Video source (file or camera)
cap = cv2.VideoCapture("video.mp4")

count_line_position = 550
min_width_rect = 80
min_height_rect = 80

# Background subtractor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def center_handle(x, y, w, h):
    cx = x + int(w / 2)
    cy = y + int(h / 2)
    return cx, cy

detect = []
offset = 6
counter = 0

print("Vehicle counting started...")

while cap.isOpened():
    ret, frame1 = cap.read()
    if not ret:
        print("Video processing completed.")
        break

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if w < min_width_rect or h < min_height_rect:
            continue

        center = center_handle(x, y, w, h)
        detect.append(center)

        for cx, cy in detect:
            if (count_line_position - offset) < cy < (count_line_position + offset):
                counter += 1
                detect.remove((cx, cy))
                print(f"Vehicle Count: {counter}")

                # Write output to file (proof for cloud)
                with open("vehicle_count.txt", "w") as f:
                    f.write(str(counter))

    # Slow loop slightly (optional)
    time.sleep(0.01)

cap.release()
print("Final Vehicle Count:", counter)
