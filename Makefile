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
	start_calculate

.PHONY: install_requirements
install_requirements:
	pip install -r requirements.txt
