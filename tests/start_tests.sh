python3.10 -m pytest \
 --no-header \
 -rfp \
 --cov \
 --cov-report html:tests/coverage \
 --cov-report xml:tests/coverage/coverage.xml \
 --junitxml=tests/coverage/report.xml \
 tests/
