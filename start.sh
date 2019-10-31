python -m virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python setup.py install
gunicorn -t 200 --workers=50 -b 0.0.0.0:$PORT src.app:app --log-level=debug