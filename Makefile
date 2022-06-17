.PHONY: all
all: start_calculate compress_data read_data install_requirements

.PHONY: start_calculate
start_calculate:
	@echo "Start calculate"
	python main.py
	@echo "Calculate done"

.PHONY: compress_data
compress_data:
	@echo "Compress data"
	zip -r Primos.zip Primos
	@echo "Compress done"

.PHONY: read_data
read_data:
	@bat Primos/Informacion.csv

.PHONY: install_requirements
install_requirements:
	pip install -r requirements.txt

.PHONY: get_information
get_information:
	@python -c 'from src.save_information import read_information; read_information()' | bat -l "json"