#!/bin/bash
cd /home/ec2-user/patogram
docker-compose build --no-cache
docker-compose up -d
