phony: test read-cov
test:
	pytest -vvv --cov=. --cov-fail-under=100 --cov-branch --cov-report term-missing .
read-cov:
	python -m read_coverage
coverage:
	coverage run -m test_sut --branch
debug:
	python -m debugpy --listen 0.0.0.0:5700 --wait-for-client -m pytest -vvv --cov=. --cov-fail-under=100 --cov-branch --cov-report term-missing .
debug2: 
	python -m debugpy --listen 0.0.0.0:5700 --wait-for-client -m coverage run -m test_sut --branch
