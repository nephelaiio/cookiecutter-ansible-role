.PHONY: install test

USER_NAME ?= nephelaiio
ROLE_NAME ?= tree

clean:
	rm -rf "${USER_NAME}.${ROLE_NAME}"

install:
	@type poetry >/dev/null || pip3 install poetry
	@poetry install

test: install
	USER_NAME=${USER_NAME} \
	ROLE_NAME=${ROLE_NAME} \
	poetry run pytest -s
