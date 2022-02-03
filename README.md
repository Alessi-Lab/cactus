# cactus

Providing backend for https://github.com/noatgnu/curtain

## Requirements

- Python >= 3.9

## Manual installation

`pip install -r requirements.txt`

`python main.py --port=8000`

The backend would be started and listening at port 8000.

While `tornado` the web framework used for building of `cactus` is fully production ready by itself, it is only a single thread webserver. You may want to run multiple servers at multiple ports and have them served through an `nginx` reverse proxy.

User upload files could be found in the `files` folder while the sqlite db is in the `db` folder. 