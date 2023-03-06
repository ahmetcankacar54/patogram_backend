#!/bin/bash
cd /home/ec2-user/patogram_backend
docker-compose build --no-cache
docker-compose up -d
