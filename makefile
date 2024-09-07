.PHONY: activate python 🐍 environment

activate:
	if [ -d "venv" ]; then \
		echo "Python 🐍 environment was activated"; \
		source venv/bin/activate; \
	else \
		 echo "The folder environment doesn't exist"; \
		 python3 -m venv venv; \
		 source venv/bin/activate; \
		 echo "The environment folder was created and the python 🐍 environment was activated"; \
	fi

install:
	pipenv install
	sleep 5
	pipenv shell

migration:
	python3 manage.py makemigrations