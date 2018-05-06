venv:
	@python --version >/dev/null 2>&1 || (echo "Python is not installed. Please install Python 3.6."; exit 1);
ifeq ($(shell python --version 2>/dev/null | awk '{print substr($$0, 8, 3)}'), 3.6)
	python -m venv venv
	. venv/Scripts/activate; python -m pip install --upgrade pip
else
	@(echo "A version of Python older than 3.6 is installed. Please install Python 3.6."; exit 1)
endif

install: venv
	. venv/Scripts/activate; pip install -r requirements.txt

.PHONY: install