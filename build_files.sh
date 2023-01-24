echo "BUILD START"

python3.10 -m pip install -r requirments.txt
python3.10 manage.py collectstatic --noinput --clear

echo "END BUILD"
