.PHONY: all clean

TRAIN_URL = "https://www.kaggle.com/c/titanic/download/train.csv"
TEST_URL = "https://www.kaggle.com/c/titanic/download/test.csv"

all: data/raw/train.csv data/raw/test.csv

clean:
	rm -f data/raw/*.csv
	
data/raw/train.csv:
	python src/data/download.py $(TRAIN_URL) $@
	
data/raw/test.csv:
	python src/data/download.py $(TEST_URL) $@