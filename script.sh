#!/bin/bash
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
value=$(curl -s https://www.marketwatch.com/investing/index/nik/charts?countryCode=JP | grep -o '<bg-quote class="value">[0-9]\+.[0-9]\+</bg-quote>' | sed 's/<bg-quote class="value">//;s/<\/bg-quote>//')
echo "$timestamp $value" >> data.txt


