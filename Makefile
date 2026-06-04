install:
	pip install -r requirements.txt

test:
	pytest -q

e2e:
	python3 scripts/run_all_experiments.py

e2e-deepmimo:
	python3 -c "from oulu_mimo.deepmimo_adapter import generate_deepmimo_config; print(generate_deepmimo_config())"

e2e-sionna:
	python3 -c "from oulu_mimo.sionna_adapter import generate_sionna_config; print(generate_sionna_config())"
