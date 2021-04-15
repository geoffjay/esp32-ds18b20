#!/bin/bash

esptool.py \
    --port "${AMPY_PORT}" \
    --baud 256000 \
    erase_flash

esptool.py \
    --chip esp32 \
    --port "${AMPY_PORT}" \
    --baud 256000 write_flash \
    --flash_mode dio 0x1000 \
    assets/firmware/"${FIRMWARE_RELEASE}"
