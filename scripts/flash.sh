#!/bin/bash

esptool.py \
    --port /dev/ttyUSB0 \
    --baud 460800 \
    erase_flash

esptool.py \
    --chip esp32 \
    --port /dev/ttyUSB0 \
    --baud 460800 write_flash \
    -z 0x1000 \
    assets/firmware/$FIRMWARE_RELEASE
