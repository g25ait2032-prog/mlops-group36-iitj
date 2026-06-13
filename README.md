# MLOps Group 36 — IIT Jodhpur

> **SMS Spam Classification** using `distilbert-base-uncased`, fine-tuned on Kaggle across four hyperparameter versions, tracked with W&B, served via Docker (GHCR & Docker Hub), and automated through GitHub Actions.

[![CI](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/ci.yml/badge.svg)](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/ci.yml)
[![Inference](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/inference.yml/badge.svg)](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/inference.yml)

---

## Group Members

| Name | Roll Number | Contributions |
|---|---|---|
| Duggirala Vnaga Ananth | G25AIT2032 | Repository setup, workflow orchestration, model training (v1–v4), W&B tracking, Docker/GHCR, GitHub Actions CI/CD |
| Anukumar K | G25AIT2016 | Dataset preparation, data cleaning, preprocessing pipeline, data versioning |
| Shrikrishna Tripathi | G25AIT2103 | Model experimentation and fine-tuning across versions, HF Hub deployment |
| Sudeb Ghosh | G25AIT2113 | Inference pipeline, evaluation (adversarial + latency), Dockerization, final reporting |

---

## Live Links

| Resource | URL |
|---|---|
| GitHub Repository | [github.com/g25ait2032-prog/mlops-group36-iitj](https://github.com/g25ait2032-prog/mlops-group36-iitj) |
| Kaggle Version 3 | [https://www.kaggle.com/code/g25ait2032/mlops-group36-final-v3](https://www.kaggle.com/code/g25ait2032/mlops-group36-final-v3) |
| HF Model — v1 | [nagaananth/MLOPS_group-v1](https://huggingface.co/nagaananth/MLOPS_group-v1) |
| HF Model — v2 ★ Best | [nagaananth/MLOPS_group-v2](https://huggingface.co/nagaananth/MLOPS_group-v2) |
| HF Model — v3 | [nagaananth/MLOPS_group-v3](https://huggingface.co/nagaananth/MLOPS_group-v3) |
| HF Model — v4 | [nagaananth/MLOPS_group-v4](https://huggingface.co/nagaananth/MLOPS_group-v4) |
| W&B Project Dashboard | [wandb.ai/g25ait2032-iit-jodhpur/MLOPS_Group](https://wandb.ai/g25ait2032-iit-jodhpur/MLOPS_Group) |
| Docker Image (GHCR) | https://github.com/g25ait2032-prog/MLOPS_Group/pkgs/container/mlops_group-inference  |
| Docker Image (Hub) | `dvnananth/mlops-group36:v1` |
| GitHub Actions | [Actions Dashboard](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions) |

---

## Pipeline Status

| Task | Owner | Status |
|---|---|---|
| Task 1 — GitHub repo setup | G25AIT2032 | ✅ Done |
| Task 2 — Data prep & normalisation | G25AIT2016 | ✅ Done |
| Task 3 — Model / tokeniser load | G25AIT2032 | ✅ Done |
| Task 4 — Fine-tune v1/v2/v3/v4 (Kaggle) | G25AIT2103 | ✅ Done |
| Task 5 — Push models to HF Hub | G25AIT2103 | ✅ Done |
| Task 6 — Dockerfile & GHCR push | G25AIT2032 | ✅ Done |
| Task 7 — GitHub Actions CI + Inference | G25AIT2032 | ✅ Done |
| Task 8 — W&B experiment comparison | G25AIT2032 | ✅ Done |
| Task 9/10 — Inference & evaluation | G25AIT2113 | ✅ Done |

---

## Project Structure

```
mlops-group36-iitj/
├── src/
│   ├── prepare_data.py         # Task 2 — Data cleaning & normalisation
│   ├── inference.py            # Task 6 & 7 — Inference script (HF Hub → prediction)
│   └── evaluate.py             # Task 10 — Local evaluation helper
├── notebooks/
│   └── MLOps_Group36_Final.ipynb   # Tasks 3–10 — Full training notebook (v1/v2/v3/v4)
├── outputs/
│   ├── experiment_results.csv
│   ├── confusion_matrix.png
│   ├── version_comparison.png
│   └── run_summary.json
├── .github/
│   └── workflows/
│       ├── ci.yml              # Task 7.1 — CI linting (flake8) on push to main
│       └── inference.yml       # Task 7.2 — Manual inference trigger + GHCR push
├── data/
│   └── id2label.json           # Label mapping (only small file committed)
├── Dockerfile                  # Task 6 — Inference container
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Model

**`distilbert-base-uncased`** — a distilled version of BERT retaining 97% of language understanding at 40% smaller size (~66M parameters). Chosen because it:

- Fits within Kaggle free-tier GPU quota (T4 x2)
- Is well-suited to short, noisy SMS text
- Achieves fast inference suitable for CPU deployment

---

## Dataset

**UCI SMS Spam Collection** loaded via HuggingFace `datasets` (`sms_spam`).

| Split | Samples | Ham % | Spam % |
|---|---|---|---|
| Train (70%) | 3,611 | ~87.5 | ~12.5 |
| Validation (15%) | 774 | ~87.5 | ~12.5 |
| Test (15%) | 774 | ~87.5 | ~12.5 |

**Cleaning steps:** lowercased → whitespace normalised → 415 duplicates removed → zero-leakage stratified split (verified with set-intersection checks).

---

## Experiment Comparison

| Version | LR | Epochs | Batch | Accuracy | F1 Weighted | F1 Macro | Val Loss |
|---|---|---|---|---|---|---|---|
| v1 | 3e-5 | 3 | 16 | 0.9935 | 0.9935 | 0.9849 | 0.0539 |
| v2 ★ Best | 2e-5 | 5 | 32 | 0.9935 | 0.9935 | 0.9851 | **0.0292** |
| v3 | 2e-5 | 5 | 32 | 0.9935 | 0.9935 | 0.9851 | 0.0376 |
| v4 | 1e-5 | 4 | 16 | — | — | — | — |

**v2** selected as the best model (lowest validation loss: 0.0292). All runs tracked in the [W&B dashboard](https://wandb.ai/g25ait2032-iit-jodhpur/MLOPS_Group).

---

## Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/g25ait2032-prog/mlops-group36-iitj.git
cd mlops-group36-iitj

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Running Each Step

### Step 1 — Prepare Data (local)

```bash
python src/prepare_data.py
# Outputs: data/train.csv, data/validation.csv, data/test.csv,
#          data/id2label.json, data/label2id.json
```

### Step 2 — Train on Kaggle

1. Upload `notebooks/MLOps_Group36_Final.ipynb` into a new Kaggle Notebook.
2. Upload `data/train.csv`, `data/test.csv`, `data/id2label.json` as a Kaggle Dataset.
3. Enable GPU: **Settings → Accelerator → GPU T4 x2**.
4. Add Kaggle Secrets: `WANDB_API_KEY_gr`, `HF_TOKEN_gr`, `GITHUB_TOKEN`.
5. Set `VERSION = "v1"` in the config cell and run. Repeat for `"v2"`, `"v3"`, `"v4"`.

### Step 3 — Run Inference Locally

```bash
export HF_TOKEN=your_token
export HF_MODEL=nagaananth/MLOPS_group-v2
export INPUT_TEXT="Free prize! Click now to claim."
python src/inference.py
```

### Step 4 — Docker

```bash
# Pull from GHCR (no build needed)
docker pull ghcr.io/g25ait2032-prog/mlops_group-inference:latest
docker run --rm \
  -e HF_TOKEN=your_token \
  -e INPUT_TEXT="Win a free car now!" \
  ghcr.io/g25ait2032-prog/mlops_group-inference:latest

# Or pull from Docker Hub
docker pull dvnananth/mlops-group36:v1
docker run --rm \
  -e INPUT_TEXT="Win a free car now!" \
  dvnananth/mlops-group36:v1
```

### Step 5 — GitHub Actions Inference (manual)

1. Go to **Actions → Inference → Run workflow**.
2. Enter the text you want to classify.
3. Check the run logs for the predicted label and confidence score.

---

## GitHub Secrets Required

| Secret | Description |
|---|---|
| `HF_TOKEN` | Hugging Face write token |
| `HF_MODEL` | HF repo ID (e.g. `nagaananth/MLOPS_group-v2`) |
| `WANDB_API_KEY` | W&B API key |
| `GITHUB_TOKEN` | Auto-provided by GitHub Actions |

Add via: **Settings → Secrets and Variables → Actions → New repository secret**

---

## Inference Output Examples

```json
{
  "text": "Congratulations! You've won a free iPhone. Click here now.",
  "label": "spam",
  "confidence": 0.9804
}
```

```json
{
  "text": "Hey, are we meeting at 5 PM today?",
  "label": "ham",
  "confidence": 0.9982
}
```

---

## Notes

- Training is done **only on Kaggle** — GitHub Actions handles CI (linting) and inference only.
- Large data files (`train.csv`, `test.csv`) are excluded via `.gitignore`; only `id2label.json` is committed.
- All four experiment versions (v1–v4) are visible in the W&B dashboard — project visibility is set to **Public**.
- All links are publicly accessible.
