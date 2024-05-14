#!/bin/bash

TARGET=$1

while :
do
    cat /sys/fs/cgroup/memcos/memory.stat | grep -e anon_thp -e anon >> ${TARGET}/memory_stat.txt
    cat /sys/fs/cgroup/memcos/memory.hotness_stat >> ${TARGET}/hotness_stat.txt
    cat /proc/vmstat | grep pgmigrate_su >> ${TARGET}/pgmig.txt
    sleep 1
done
