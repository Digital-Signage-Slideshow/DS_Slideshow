# DS-Slideshow
A web based digital signage application

<b>Dependancies:</b><br>
Python3, Flask<br>

<b>Usage: </b><br>
Clone the repository and open a screen or other utility to keep the program running in the background. Run controller.py in the DS-Slideshow folder. If needed, this application can be run in Apache or Nginx.<br>
You should see the loading text:
```shell
pi@raspberrypi:~ & python3 controller.py

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

The application is hosted on port 5001, open  e.g. 127.0.0.1:5001<br>
go to 127.0.0.1:5001/setup to get into the setup menu for the slideshow. Remove the deleteMe.jpg file and add your own content.<br>
