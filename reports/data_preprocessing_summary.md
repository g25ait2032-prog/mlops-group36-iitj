# Data Preprocessing Summary

## Owner
Anu Kumar - G25AIT2016

## Dataset
SMS Spam Collection dataset loaded using Hugging Face datasets.

## Task
Binary text classification:
- ham
- spam

## Cleaning Decisions
- Converted SMS text to lowercase.
- Replaced URLs with the token `url`.
- Removed extra spaces.
- Removed empty or missing text rows.
- Removed duplicate SMS messages.
- Kept numbers and punctuation because they may be useful spam indicators.

## Dataset Statistics
- Original rows: 5574
- Missing text rows: 0
- Missing label rows: 0
- Duplicate rows removed: 415
- Final rows after cleaning: 5159

## Class Distribution
{'ham': 4517, 'spam': 642}

## Split Strategy
Used stratified train, validation, and test split so that the ham/spam ratio stays similar in each split.

- Train rows: 3611
- Validation rows: 774
- Test rows: 774

## Files Created
- data/processed/train.csv
- data/processed/validation.csv
- data/processed/test.csv
- data/id2label.json
- data/label2id.json

Only mapping files are committed to GitHub. Processed CSV files are generated locally and ignored using .gitignore.
