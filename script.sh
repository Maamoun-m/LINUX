#!/bin/bash

# Retrieve current value of Nikkei 225 index
value=$(curl https://www.marketwatch.com/investing/index/nik/charts?countryCode=JP | grep '<bg-quote class="value">.*</bg-quote>' | sed 's/<bg-quote class="value">//g;s/<\/bg-quote>//g')

# Append value to file
echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") $value" >> nikkei.txt

