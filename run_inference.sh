#!/bin/bash

tlt detectnet_v2 inference \
  -k tlt_encode \
  -e /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/specs/detectnet_v2_inference_config.txt \
  -i /workspace/tlt-experiments/mask-detect-tlt/data/test/images \
  -o /workspace/tlt-experiments/mask-detect-tlt/data/inference_on_test
