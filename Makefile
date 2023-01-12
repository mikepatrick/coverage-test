phony: test read-cov
test:
	pytest -vvv --cov=. --cov-fail-under=100 --cov-branch --cov-report term-missing .
read-cov:
	python -m read_coverage
coverage:
	coverage run -m test_sut --branch
debug:
	python -m debugpy --listen 0.0.0.0:5700 --wait-for-client -m collect_coverage
collect:
	python -m collect_coverage
clean:
	rm -f .coverage
	rm -rf __pycache__
	rm -rf .pytest_cache
