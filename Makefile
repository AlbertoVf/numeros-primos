.PHONY: all
all: run compress_data build get_information generate_commit

.PHONY: run
run:
	@echo "Start calculate"
	python main.py
	@echo "Calculate done"
	make generate_commit

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
	@python -c 'from src.save_information import read_information; read_information()' > info.json
	@bat  info.json Primos/Informacion.csv
	rm info.json

.PHONY:generate_commit
generate_commit:
	@git add Primos/Informacion.csv data.json
	@git commit -m "docs(numbers): Generate new ranges"