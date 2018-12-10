init:
ifeq ($(TRAVIS), true)
		pip install pipenv
		pipenv install --dev
		pip install .
else
		pipenv install --dev
		pre-commit install
endif

test:
	py.test -rpsf --cov=mass_replace --cov-report term-missing

lint:
ifeq ($(TRAVIS_PYTHON_VERSION), 2.7)
		echo "Skip linting for Python2.7"
else
		prospector --output-format grouped --with-tool pyroma --strictness medium
endif

format:
	black .

check_format:
ifeq ($(TRAVIS_PYTHON_VERSION), 3.7)
		black . --check
else
		echo "Only check format on Python3.7"
endif

pre:
	pre-commit run --all-files
