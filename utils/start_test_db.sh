#!/usr/bin/env bash
docker run \
--name test-database \
-p 5432:5432 \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_DB=slideshow \
-e POSTGRES_USER=slideshow_user \
-d postgres:latest