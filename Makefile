.PHONY: precommit
precommit:
	pre-commit run --all-file --show-diff-on-failure

.PHONY: lint
lint:
	python -m pylint --version
	find . -type f -name "*.py" | xargs python -m pylint

.PHONY: tests
tests:
	python -m pytest --version
	coverage run -m pytest
	coverage report -m

.PHONY: black
black:
	python -m black --version
	python -m black .

.PHONY: ci
ci: precommit tests

.PHONY: up
up: 
	docker-compose up