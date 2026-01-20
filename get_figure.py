import os
from tqdm import tqdm

import cv2

def main():
    pass

def flip(images_path="demo_out/01_20_13_01/295"):
    # flip image horizontally
    out_path = f"{images_path}/hand_flipped"
    os.makedirs(out_path, exist_ok=True)
    hand_paths = [p for p in os.listdir(images_path) if "_hand.png" in p]
    for hand_path in tqdm(hand_paths):
        in_path = os.path.join(images_path, hand_path)
        img = cv2.imread(in_path, cv2.IMREAD_UNCHANGED)  # keep alpha if present
        if img is None:
            print(f"Skipping (failed to read): {in_path}")
            continue
        flipped = cv2.flip(img, 1)  # 1 = horizontal flip
        # out_path = in_path.replace("hand", "hand_flipped")
        img_out_path = f"{out_path}/{hand_path}"
        
        ok = cv2.imwrite(img_out_path, flipped)


if __name__ == "__main__":
    # main()
    flip()