install:
	@poetry install
	

brain-games:
	@poetry run brain-games


publish:
	poetry publish --dry-run


package-install:
	pipx install dist/*.whl


lint:
	@poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build



.PHONY: test build publish lint selfcheck check install test lint selfcheck check build