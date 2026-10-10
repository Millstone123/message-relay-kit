.PHONY: summary inventory test

summary:
	python3 -c 'import json; data=json.load(open("data/events.json")); print("events=%d" % len(data))'
	python3 summarize.py

inventory:
	python3 -c 'import json; data=json.load(open("data/events.json")); print("events=%d" % len(data))'
	python3 tools/inspect.py

test:
	python3 -m unittest discover -v
