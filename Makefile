.PHONY: setup test audit status
setup:
	python -m pip install -e '.[dev]'
test:
	pytest -q
	python -m compileall -q src
audit:
	researchos audit-evidence literature/evidence/claims.json
	researchos audit-journals journals/profiles
status:
	researchos status
