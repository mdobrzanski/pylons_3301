clean:
	find . -name "*.pyc" -delete
	find . -name "*.c" -delete
	find . -name "*.so" -delete
	rm -rf *.so
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist