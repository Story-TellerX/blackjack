path := cd ./data-analysis-app
pyrun := pipenv run
venv := .venv

install: $(venv)
$(venv): $(venv)/bin/activate
$(venv)/bin/activate: Pipfile.lock
	$(call log, "Installing dependencies ...")
	pipenv --version &> /dev/null || pip install pipenv
	PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
	touch $(venv)/bin/activate
	$(call log, "Installing dependencies Done")


rules :=	install				\

.PHONY: $(rules)
.SILENT: $(rules) $(venv)/bin/activate

run:
	$(pyrun) python main.py
