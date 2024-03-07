#!/bin/sh

mkdir -p /app

while true
do
	echo "Writing log to a file"
  echo '{"app":"file-myapp"}' >> /app/example-log.log
	sleep 5
done