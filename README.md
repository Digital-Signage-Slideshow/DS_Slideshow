# Digital Signage Slideshow

[![Actions Status](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/actions/workflows/push.yml/badge.svg)](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/actions)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Flask Development Server](#flask-development-server)
  * [Docker](#docker)
* [Roadmap](#roadmap)
 * [Upcoming Features](#upcoming-features)
 * [Features in Discussion](#features-in-discussion)
* [Images](#images)
* [Contributing](#contributing)
* [License](#license)

## About the Project

![Screenshot](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/blob/bootstrap/.github/content_screenshot.PNG)

DS Signage is a lightweight flask based Digital Signage system I designed for use on Raspberry Pi or similar. To get started, clone or fork this repo. For instructions on getting started, follow the usage steps below. For contributing guidelines, please see the contributing section near the end of the README.

### Built With

* Python3
* Flask
* Bootstrap
* Font Awesome

See our dependancies for more details on the depencies of this project.

## Getting Started

### Flask Development Server

This method is not recommended over the Docker hosting for any reason unless developing. Flask's inbuilt development server is not designed for use in a production environment.

To launch the Flask developement server, you should navigate to the DS-Slideshow directory (shown below).

```bash
> ls
migrations  slideshow display static  templates user  config.py docker-compose.yml  Dockerfile  README.md requirements.txt  wsgi.py
```

and execute the following commands. The environment variables are stored in the .flaskenv file and will be automatically loaded. It is also recommended to launch this application in a Python virtual environment. (venv is not included in the requirements.txt and will need to be manually configured)

```
> python3 -m pip install -r requirements.txt
...
> flask run

 * Serving Flask app "wsgi" (lazy loading)
 * Environment: development
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

opening 127.0.0.1:5001/setup on the host machine will launch into the configuration screen.

### Docker

This project also comes equipped with a premade docker-compose setup. [Docker](https://www.docker.com/products/docker-desktop) is required for this method of running. This is recommended over the Flask Developemnt server due to serving on gunicorn.
This docker container is configured to automatically restart on startup so your slideshow will always be available. After installing docker, the slideshow can be run.

Navigate to the DS-Slideshow directory (shown below).

```bash
> ls
migrations  slideshow display static  templates user  config.py docker-compose.yml  Dockerfile  README.md requirements.txt  wsgi.py
```

and run the following:

```bash
docker-compose up -d --build
```

The first time running may take some time as the docker container downloads and installs all prerequisites. The docker container is entirely self contained so the requirements.txt file does not need to be run seperately, this is all handled by the docker-compose.yml and Dockerfile configuration.

running docker ps will reveal the state of the docker container (formatted example shown below).

| CONTAINER ID | IMAGE | COMMAND | CREATED | STATUS | PORTS | NAMES |
|--------------|-------|---------|---------|--------|-------|-------|
| 9c0fff0f1256 | dsslideshow | "gunicorn -w 4 --bin…" | 11 minutes ago | Up About a minute | 0.0.0.0:80->5000/tcp | ds-slideshow_dsslideshow_1 |

to halt the running of the program you can simply navigate to the DS-Slideshow directory again and execute the command:

```bash
docker-compose down
```

## Roadmap

### Upcoming Features

These are the features that are being actively considered/ worked on. 

* Video/ Gif support. There is an open branch for this feature! I am currently fine-tuning the behaviour.
* Rearranging the position of links/ images uploaded. Currently, there is no way of rearranging the order of your slides. This is a feature I am working on!

### Features in Discussion

These features are much further down the line. There isn't even an issue open for most of these. If you would like to try and take on one of these, please feel free to fork the repo!

* Different content for different screens.

## Images

A collection of screenshots from our gallery.

![content](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/blob/bootstrap/.github/content_screenshot.PNG)
![no-content](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/blob/bootstrap/.github/no_content_screenshot.PNG)
![upload-content](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/blob/bootstrap/.github/upload_content_screenshot.PNG)
![login](https://github.com/Digital-Signage-Slideshow/DS_Slideshow/blob/bootstrap/.github/login_screenshot.PNG)

## Contributing
This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to create a merge request or issue to discuss changes.

## License
This code is available under the [MIT](https://choosealicense.com/licenses/mit/) licence
