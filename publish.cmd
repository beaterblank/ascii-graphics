del /s dist
update.py
python setup.py bdist_wheel sdist
twine upload dist/*