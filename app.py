import os
from Thetechblog import app

if __name__=='__main__':
    debug = os.environ.get('FLASK_DEBUG', '1') == '1'
    app.run(debug=True)
