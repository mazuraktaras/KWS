import sys

sys.path.insert(0, '/home/ubuntu/app/KWS')
sys.path.insert(1, '/home/ubuntu/app/KWS/kwsapp')

from kwsapp import app

if __name__ == '__main__':
    app.run()

# export FLASK_APP=kws.py
# export FLASK_ENV=development
