install:
	@poetry install
	

brain-games:
	@poetry run brain_games

brain-even:
	@poetry run brain_even

publish:
	poetry publish --dry-run


package-install: build
	pipx install dist/*.whl

package-uninstall:
	pipx uninstall hexlet-code

lint:
	@poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

test:
	poetry run pytest brain_games tests



.PHONY: test build publish lint selfcheck check install test lint selfcheck check build