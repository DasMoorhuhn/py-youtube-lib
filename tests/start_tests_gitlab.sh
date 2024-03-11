apk add --update wget
pip3.10 install -r requirements.txt
sh tests/start_tests.sh

cp tests/coverage/coverage.xml ./coverage.xml
cp tests/coverage/report.xml ./report.xml

wget -q https://gitlab.com/DasMoorhuhn/autopicture-v3/-/raw/main/tests/get_coverage_percent.py?ref_type=heads  -O- | python3.10
