.PHONY: all
all: run compress_data build get_information

.PHONY: run
run:
	@python -c 'from src.save_information import read_information; read_information()' | bat -l "json"
	@echo "Start calculate"
	python main.py
	@echo "Calculate done"
	@git add Primos/Informacion.csv data.json
	@git commit -m "docs(numbers): Calculate new ranges"

.PHONY: compress_data
compress_data:
	@echo "Compress data"
	zip -r Primos.zip Primos
	@echo "Compress done"

.PHONY: build
build:
	pip install -r requirements.txt

.PHONY: get_information
get_information:
	@bat Primos/Informacion.csv