# define name of virtual environment directory
VENV := venv

my_debug:
	@echo "==== $(OS) ===="

# different procedure for Windows and other OS
ifeq ($(OS),Windows_NT)
	py.exe -m venv $(VENV)
	./$(VENV)/Scripts/python.exe -m pip install .
else
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install .
endif

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

