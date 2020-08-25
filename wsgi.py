from slideshow import create_app

app = create_app()

__author__ = 'Harry Lees'
__date__ = '08.08.2020'

if __name__ == '__main__':
    # Remove host='0.0.0.0' on production environment
    app.run(host='0.0.0.0')
