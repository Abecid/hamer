#!/usr/bin/env bash
set -euo pipefail

PYTHON="/home/alee00/anaconda3/envs/hamer/bin/python"

INPUT_ROOT="./input"
OUT_ROOT="demo_out"

mkdir -p "$OUT_ROOT"

# Iterate over immediate subdirectories of ./input
find "$INPUT_ROOT" -mindepth 1 -maxdepth 1 -type d -print0 | while IFS= read -r -d '' subdir; do
  echo "==> Processing: $subdir"
  "$PYTHON" demo.py \
    --img_folder "$subdir" \
    --out_folder "$OUT_ROOT" \
    --batch_size 48 \
    --side_view \
    --save_mesh \
    --full_frame
done
