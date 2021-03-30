#!/bin/bash

esptool.py \
    --chip esp32 \
    --port /dev/tty.usbserial-0001 \
    --baud 460800 write_flash \
    -z 0x1000 \
    assets/firmware/$FIRMWARE_RELEASE
