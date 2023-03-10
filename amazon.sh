#!/bin/bash

response=$(curl -s https://ip-ranges.amazonaws.com/ip-ranges.json)
prefixes=$(echo $response | jq -r '.prefixes[] | .ip_prefix')
for prefix in $prefixes; do
  ip=$(echo $prefix | cut -d/ -f1)
  echo $ip >> list.txt
  echo "$ip"
done
