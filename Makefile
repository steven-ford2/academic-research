.PHONY: setup test audit status
setup:
	python -m pip install -e '.[dev]'
test:
	pytest -q
audit:
	researchos audit-evidence literature/evidence/claims.json
	researchos audit-journals journals/profiles
status:
	researchos status
