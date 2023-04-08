runnetcheck:
	poetry run netcheck

lint:
	poetry run flake8 netcheck

black:
	poetry run black netcheck

isort:
	poetry run isort netcheck

test:
	poetry run pytest --cov=netcheck --cov-report xml tests/

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl
