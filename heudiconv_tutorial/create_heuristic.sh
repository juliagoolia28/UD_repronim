#!/bin/bash
docker run --rm -it \
-v /Users/julieschneider/repronim/UD_repronim/heudiconv_tutorial:/data:ro \
-v /Users/julieschneider/repronim/UD_repronim/heudiconv_tutorial/BIDS:/output \
nipy/heudiconv:latest \
-d /data/{subject}/{session}/*/*.IMA \
-s sub_01 \
--ses 20200813_171810_110000 \
-f convertall \
-c none \
-o /output

