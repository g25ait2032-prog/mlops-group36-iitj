import json
import os

import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split

SEED = 42
DATA_DIR = "data"


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("Loading SMS Spam dataset from Hugging Face...")

    df = (
        load_dataset("sms_spam", split="train")
        .to_pandas()
        .rename(columns={"sms": "text"})
    )

    print(f"Raw samples: {len(df):,}")

    # Clean data
    df = df.dropna(subset=["text", "label"])

    df["text"] = (
        df["text"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    before_dedup = len(df)
    df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    print(f"Duplicates removed: {before_dedup - len(df):,}")
    print(f"Remaining samples : {len(df):,}")

    # Label mappings
    label2id = {"ham": 0, "spam": 1}
    id2label = {0: "ham", 1: "spam"}

    # Train / Validation / Test split (70 / 15 / 15)
    train_df, temp_df = train_test_split(
        df,
        test_size=0.30,
        random_state=SEED,
        stratify=df["label"],
    )

    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.50,
        random_state=SEED,
        stratify=temp_df["label"],
    )

    train_df = train_df.reset_index(drop=True)
    val_df = val_df.reset_index(drop=True)
    test_df = test_df.reset_index(drop=True)

    # Leakage checks
    train_texts = set(train_df["text"])
    val_texts = set(val_df["text"])
    test_texts = set(test_df["text"])

    assert not (train_texts & val_texts), "Train/Validation leakage detected"
    assert not (train_texts & test_texts), "Train/Test leakage detected"
    assert not (val_texts & test_texts), "Validation/Test leakage detected"

    print("Leakage checks: PASSED")

    # Save datasets
    train_df.to_csv(os.path.join(DATA_DIR, "train.csv"), index=False)
    val_df.to_csv(os.path.join(DATA_DIR, "validation.csv"), index=False)
    test_df.to_csv(os.path.join(DATA_DIR, "test.csv"), index=False)

    # Save label mappings
    with open(os.path.join(DATA_DIR, "label2id.json"), "w") as f:
        json.dump(label2id, f, indent=2)

    with open(os.path.join(DATA_DIR, "id2label.json"), "w") as f:
        json.dump({str(k): v for k, v in id2label.items()}, f, indent=2)

    print("\n=== Dataset Split ===")
    print(f"Train      : {len(train_df):,}")
    print(f"Validation : {len(val_df):,}")
    print(f"Test       : {len(test_df):,}")

    print(f"\nDatasets saved to: {DATA_DIR}")
    print("Training data preparation completed successfully.")


if __name__ == "__main__":
    main()
