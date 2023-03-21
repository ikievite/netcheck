runnetcheck:
	poetry run netcheck

lint:
	poetry run flake8 netcheck

black:
	poetry run black netcheck
