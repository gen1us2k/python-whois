build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

deps:
	pip install twine

