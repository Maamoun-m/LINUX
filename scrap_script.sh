#!/bin/bash
echo "Time,Prix" > ~/arbitrum_prices.csv
while :
do
  curl https://www.coingecko.com/fr/pi%C3%A8ces/arbitrum> ~/arbitrum_data.txt
  prix=$(cat ~/arbitrum_data.txt | grep -m 1 -oP '(?<="price.price">)[^<]+' | tr -d '$' | tr ',' '.')
  time_now=$(date +"%Y-%m-%d %T")
  echo "$time_now,$prix" >> ~/arbitrum_prices.csv
  sleep 30 #boucle de 30 secondes
done


