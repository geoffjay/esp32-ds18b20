#!/bin/bash

esptool.py \
    --port /dev/ttyUSB0 \
    --baud 115200 \
    erase_flash

esptool.py \
    --chip esp32 \
    --port /dev/ttyUSB0 \
    --baud 115200 write_flash \
    --flash_mode dio 0x1000 \
    assets/firmware/"${FIRMWARE_RELEASE}"
