#!/bin/bash

docker run -it --rm \
	--name django \
	-w /app \
	-e TRAJAN_SERVICE_URL=http://$(ipconfig getifaddr en0):8002/ \
	-p 8000:8000 -v $(pwd):/app python ./run.sh
