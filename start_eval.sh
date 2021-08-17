#!/bin/bash

tlt detectnet_v2 evaluate \
  -k tlt_encode \
  -m /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/weights/model.tlt \
  -e /workspace/tlt-experiments/mask-detect-tlt/detectnet_v2/experiment_spec.txt