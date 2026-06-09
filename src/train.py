import os
import json
import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split

DATA_DIR = "data"
SEED = 42

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    print("Loading SMS Spam dataset from Hugging Face …")
    df = (
        load_dataset("sms_spam", split="train")
        .to_pandas()
        .rename(columns={"sms": "text"})
    )

    df = df.dropna(subset=["text", "label"])
    df["text"] = (
        df["text"].astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    label2id = {"ham": 0, "spam": 1}
    id2label = {0: "ham", 1: "spam"}

    train_df, temp_df = train_test_split(
        df, test_size=0.30, random_state=SEED, stratify=df["label"]
    )
    val_df, test_df = train_test_split(
        temp_df, test_size=0.50, random_state=SEED, stratify=temp_df["label"]
    )

    train_df.to_csv(f"{DATA_DIR}/train.csv", index=False)
    val_df.to_csv(f"{DATA_DIR}/validation.csv", index=False)
    test_df.to_csv(f"{DATA_DIR}/test.csv", index=False)

    with open(f"{DATA_DIR}/label2id.json", "w") as f:
        json.dump(label2id, f)

    with open(f"{DATA_DIR}/id2label.json", "w") as f:
        json.dump(id2label, f)

    print("Dataset prepared successfully!")

if __name__ == "__main__":
    main()
