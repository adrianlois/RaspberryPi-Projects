#!/bin/bash
 cpu=$(cat /sys/class/thermal/thermal_zone0/temp)
 echo
 echo "$(date) - $(hostname)"
 echo "========================================"
 echo "> Temp CPU: $((cpu/1000))'Cº"
 echo "> Temp GPU: $(/opt/vc/bin/vcgencmd measure_temp)"
 echo "========================================"
 echo
