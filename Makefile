runnetcheck:
	poetry run netcheck

lint:
	poetry run flake8 netcheck

black:
	poetry run black netcheck

isort:
	poetry run isort netcheck

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl
