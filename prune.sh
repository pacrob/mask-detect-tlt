#!/bin/bash

tlt detectnet_v2 prune \
  -k tlt_encode \
  -m /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/weights/model.tlt \
  -o /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/weights/model-pruned.tlt
