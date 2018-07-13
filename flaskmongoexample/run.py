from src.app import app

__author__ = 'mjd'

if __name__ == '__main__':
    app.run(host='23.254.247.82', debug=app.config['DEBUG'], port=4996)
    #app.run(host='wines.avivavino.com', debug=True, port=4995)
