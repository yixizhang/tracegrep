.PHONY: venv
venv: venv/bin/activate
venv/bin/activate:
	test -d venv || virtualenv --distribute venv
	. venv/bin/activate; pip install twine
	touch venv/bin/activate

.PHONY: build
build: venv
	python setup.py sdist
	python setup.py bdist_wheel
	. venv/bin/activate; twine upload dist/*
