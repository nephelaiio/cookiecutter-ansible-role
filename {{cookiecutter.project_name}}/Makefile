.PHONY: install lint test converge verify clean destroy reset

MOLECULE_SCENARIO ?= default

install:
	@type poetry >/dev/null || pip3 install poetry
	@poetry install

lint:
	poetry run yamllint .
	poetry run ansible-lint .
	poetry run molecule syntax

test: install lint
	poetry run molecule test -s ${MOLECULE_SCENARIO}

converge:
	poetry run molecule converge -s ${MOLECULE_SCENARIO}

verify:
	poetry run molecule verify -s ${MOLECULE_SCENARIO}

clean: destroy reset

destroy:
	poetry run molecule destroy -s ${MOLECULE_SCENARIO}

reset:
	poetry run molecule reset -s ${MOLECULE_SCENARIO}
