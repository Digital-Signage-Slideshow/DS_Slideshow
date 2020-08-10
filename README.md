# Digital Signage Slideshow

DS Signage is a lightweight flask based Digital Signage system I designed for use on my Raspberry Pi.

## Installation

This project can be installed by cloning this repo and then running the run.py script to start flask running. There is a requirements.txt file for installing the project dependancies.

```bash
python3 -m pip install -r requirements.txt
python3 run.py
```

## Usage

For small personal uses and localhost sites that aren't exposed to the internet, it may be sufficient to run using the Flask dev server, this can be done by simply running run.py and then opening the url in your browser.

```
pi@raspberrypi:~ & python3 run.py

 * Serving Flask app "controller" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: xxx-xxx-xxx
```

opening 127.0.0.1:5001/setup on the host machine will launch into the configuration screen. From here you can remove the deleteMe.png file and add any relevant files/ links from the bottom of the page. You can then open 127.0.0.1:5001 and you will see your slides rotating!

Although the project is set up to be run with the default Flask dev server, as per the Flask official docs:

"When running publicly rather than in development, you should not use the built-in development server (flask run). The development server is provided by Werkzeug for convenience, but is not designed to be particularly efficient, stable, or secure."

In light of this, it is recommended to deploy this script to a proper production server, official support and docs will come on this soon. Until then, you can read the official flask docs on [deploying an app](https://flask.palletsprojects.com/en/1.1.x/deploying/)

## Contributing
This is an open source project written almost entirely in Python3. If you would like to contribute, please feel free to create a merge request or issue to discuss changes.

## Upcoming features

Rearranging the position of links/ images uploaded. Currently, there is no way of rearranging the order of your slides. This is a feature I am working on!

## License
This code is available under the [MIT](https://choosealicense.com/licenses/mit/) licence
