#!/bin/bash

tlt detectnet_v2 train \
  -k tlt_encode \
  -r /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2 \
  -e /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/specs/detectnet_v2_train_eval_config.txt