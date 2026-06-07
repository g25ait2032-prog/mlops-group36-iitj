import json
import re
from pathlib import Path

import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"

RANDOM_SEED = 42


def clean_text(value):
    """Clean SMS text for spam classification."""
    text = "" if pd.isna(value) else str(value)

    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", " url ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def save_json(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def main():
    DATA_DIR.mkdir(exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)

    print("Loading SMS Spam dataset...")
    dataset = load_dataset("ucirvine/sms_spam", split="train")

    df = dataset.to_pandas()
    original_rows = len(df)

    df = df[["sms", "label"]].rename(columns={"sms": "text"})

    missing_text_rows = int(df["text"].isna().sum())
    missing_label_rows = int(df["label"].isna().sum())

    df["text"] = df["text"].apply(clean_text)
    df = df.dropna(subset=["label"])
    df = df[df["text"].str.len() > 0]

    duplicate_rows = int(df.duplicated(subset=["text"]).sum())
    df = df.drop_duplicates(subset=["text"], keep="first").reset_index(drop=True)

    df["label"] = df["label"].astype(int)

    id2label = {
        "0": "ham",
        "1": "spam"
    }

    label2id = {
        "ham": 0,
        "spam": 1
    }

    train_df, temp_df = train_test_split(
        df,
        test_size=0.30,
        random_state=RANDOM_SEED,
        stratify=df["label"]
    )

    validation_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=RANDOM_SEED,
        stratify=temp_df["label"]
    )

    train_df.to_csv(PROCESSED_DIR / "train.csv", index=False)
    validation_df.to_csv(PROCESSED_DIR / "validation.csv", index=False)
    test_df.to_csv(PROCESSED_DIR / "test.csv", index=False)

    save_json(id2label, DATA_DIR / "id2label.json")
    save_json(label2id, DATA_DIR / "label2id.json")

    class_distribution = (
        df["label"]
        .map(lambda label_id: id2label[str(label_id)])
        .value_counts()
        .to_dict()
    )

    summary = f"""# Data Preprocessing Summary

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
- Original rows: {original_rows}
- Missing text rows: {missing_text_rows}
- Missing label rows: {missing_label_rows}
- Duplicate rows removed: {duplicate_rows}
- Final rows after cleaning: {len(df)}

## Class Distribution
{class_distribution}

## Split Strategy
Used stratified train, validation, and test split so that the ham/spam ratio stays similar in each split.

- Train rows: {len(train_df)}
- Validation rows: {len(validation_df)}
- Test rows: {len(test_df)}

## Files Created
- data/processed/train.csv
- data/processed/validation.csv
- data/processed/test.csv
- data/id2label.json
- data/label2id.json

Only mapping files are committed to GitHub. Processed CSV files are generated locally and ignored using .gitignore.
"""

    summary_path = REPORTS_DIR / "data_preprocessing_summary.md"
    summary_path.write_text(summary, encoding="utf-8")

    print("Preprocessing completed successfully.")
    print(f"Train rows: {len(train_df)}")
    print(f"Validation rows: {len(validation_df)}")
    print(f"Test rows: {len(test_df)}")
    print(f"Saved mapping file: {DATA_DIR / 'id2label.json'}")
    print(f"Saved report summary: {summary_path}")


if __name__ == "__main__":
    main()
