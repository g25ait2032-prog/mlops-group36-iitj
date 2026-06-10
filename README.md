# End-to-End MLOps Pipeline
**MLOps | PGD AI Program | IIT Jodhpur — Group 36**

> SMS Spam Classification using **DistilBERT** (`distilbert-base-uncased`), fine-tuned on Kaggle with three hyperparameter versions, tracked with W&B, served via Docker (GHCR), and automated through GitHub Actions.

---

# Write badges into README.md and push 
readme_path = f"{REPO_PATH}/README.md"

readme_content = f"""# MLOps Group 36 — IIT Jodhpur
SMS Spam Classification · DistilBERT · Kaggle + W&B + HuggingFace + GitHub Actions

## ⚙️ GitHub Actions — Pipeline Status

| Workflow | Status |
|----------|--------|
| CI | [![CI](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/ci.yml/badge.svg)](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/ci.yml) |
| Inference | [![Inference](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/inference.yml/badge.svg)](https://github.com/g25ait2032-prog/mlops-group36-iitj/actions/workflows/inference.yml) |


## 🔗 Key Links
| Resource | URL |
|----------|-----|
| HF Model v1 | https://huggingface.co/{HF_USERNAME}/MLOPS_group-v1 |
| HF Model v2 | https://huggingface.co/{HF_USERNAME}/MLOPS_group-v2 |
| HF Model v3 | https://huggingface.co/{HF_USERNAME}/MLOPS_group-v3 |
| HF Model v4 | https://huggingface.co/{HF_USERNAME}/MLOPS_group-v4 |
| W&B Project | https://wandb.ai/{WB_ENTITY}/{WB_PROJECT} |
| Docker Hub Image | https://hub.docker.com/r/dvnananth/mlops-group36 |
| Docker Image Tag | `dvnananth/mlops-group36:v1` |
| GitHub Repository | https://github.com/g25ait2032-prog/mlops-group36-iitj |
| Index digest |sha256:4a0b5eb73254def900466d8c55f3b8d48cee25b7e9d8be69215e70161647246a  |
"""

with open(readme_path, "w") as f:
    f.write(readme_content)

# Git commit and push
import subprocess
for cmd in [
    ["git", "-C", REPO_PATH, "config", "user.name", "G25AIT2032"],
    ["git", "-C", REPO_PATH, "config", "user.email", "g25ait2032@iitj.ac.in"],
    ["git", "-C", REPO_PATH, "add", "README.md"],
    ["git", "-C", REPO_PATH, "commit", "-m", "docs: add CI/Inference badges to README [Group36]"],
    ["git", "-C", REPO_PATH, "push", "origin", "main"],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(r.stdout or r.stderr)

print("✅ README.md updated with badges and pushed to GitHub")

## 🔗 Live Links

| Resource | URL |
|---|---|
| 🐙 GitHub Repository | [`https://github.com/g25ait2032-prog/MLOPS_Group`](https://github.com/g25ait2032-prog/MLOPS_Group) |
| 🤗 HF Model — v1 ★ Best | https://huggingface.co/nagaananth/MLOPS_group-v1 |
| 🤗 HF Model — v2 | https://huggingface.co/nagaananth/MLOPS_group-v2 |
| 🤗 HF Model — v3 | https://huggingface.co/nagaananth/MLOPS_group-v3 |
| 🤗 HF Model — v4 | [`https://huggingface.co/nagaananth/MLOPS_group-v3`](https://huggingface.co/nagaananth/MLOPS_group-v3) |
| 📊 W&B Project Dashboard | `https://wandb.ai/g25ait2032-iit-jodhpur/MLOPS_Group` |
| 🐳 Docker Image (GHCR) | `ghcr.io/g25ait2032-prog/mlops_group-inference:latest` |
| 📓 Kaggle Notebook (v1) | `(https://www.kaggle.com/code/g25ait2032/9ju-gr36-mlops/edit)` |
| 📓 Kaggle Notebook (v2) | `https://www.kaggle.com/code/your-username/sms-spam-v2` |
| 📓 Kaggle Notebook (v3) | `https://www.kaggle.com/code/your-username/sms-spam-v3` |
| 📓 Kaggle Notebook (v4) | `https://www.kaggle.com/code/your-username/sms-spam-v4` |




---

## 🚦 Pipeline Status

![CI](https://github.com/g25ait2032-prog/MLOPS_Group/actions/workflows/ci.yml/badge.svg)
![Inference Pipeline](https://github.com/g25ait2032-prog/MLOPS_Group/actions/workflows/inference.yml/badge.svg)

---

## 👥 Group Members

| Name | Roll Number | Contributions |
|---|---|---|
| Ananth | G25AIT2032 | Repo setup, orchestration, model training (v1/v2/v3), W&B tracking |
| Anu Kumar | G25AIT2016 | Dataset preparation, data versioning, Git data pipeline |
| Shrikrishna Tripathi | G25AIT2103 | Model experiments (fine-tuning all versions) |
| Sudeb Ghosh| G25AIT2113 | Inference, evaluation, Docker, GitHub Actions |

---

## 📅 Gantt Chart — Task Allocation & Timeline

| Task | Owner | Week 1 | Week 2 | Week 3 | Week 4 |
|---|---|---|---|---|---|
| Task 1 — GitHub repo setup | G25AIT2032 | ██████ | | | |
| Task 2 — Data prep & normalisation | G25AIT2016 | ██████ | ██ | | |
| Task 3 — Model / tokeniser load | G25AIT2032 | | ████ | | |
| Task 4 — Fine-tune v1/v2/v3 (Kaggle) | G25AIT2103 |████ | ████ | ████ | |
| Task 5 — Push models to HF Hub | G25AIT2103 |████ | | ████ | |
| Task 6 — Dockerfile & GHCR push | G25AIT2032 | | | ████ | |
| Task 7 — GitHub Actions (CI + infer) | G25AIT2032 | | | ████ | ██ |
| Task 8 — W&B experiment comparison | G25AIT2032 | | | ████ | ██ |
| Task 9/10 — Inference & evaluation | G25AIT2113 |████ | |████ | ████ |
| Report & README | G25AIT2113 | | | | ████ |

> **Legend:** ██ = active work period. Each "Week" ≈ one sprint; overlap is intentional for review.

---

## 📁 Project Structure

```
MLOPS_Group/
├── src/
│   ├── prepare_data.py      # Task 2 — Data cleaning & normalisation
│   ├── inference.py         # Task 6 & 7 — Inference script (HF Hub → prediction)
│   └── evaluate.py          # Optional — local evaluation helper
├── notebooks/
│   └── group-36-mlops.ipynb  # Tasks 1-10 — Full pipeline notebook
├── .github/
│   └── workflows/
│       ├── ci.yml           # Task 7.1 — CI linting on push to develop
│       └── inference.yml    # Task 7.2 — Manual inference trigger
├── data/
│   ├── id2label.json        # Label mapping
│   └── data_manifest.json   # SHA-256 hashes + row counts for each split
├── Dockerfile               # Task 6 — Inference container
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧠 Model

**`distilbert-base-uncased`** — a distilled version of BERT that retains 97% of language understanding at 40% smaller size (~66 M parameters, ~265 MB). Chosen because it:

- Fits within Kaggle free-tier GPU quota (T4 x2)
- Is well-suited to short, noisy SMS text
- Has a clear, well-documented HF model card

---

## 📊 Dataset

**UCI SMS Spam Collection** loaded via `datasets` (`sms_spam`).

| Split | Samples | Ham % | Spam % |
|---|---|---|---|
| Train (70 %) | ~3,611 | 86.6 | 13.4 |
| Validation (15 %) | ~774 | 86.6 | 13.4 |
| Test (15 %) | ~774 | 86.6 | 13.4 |

**Cleaning steps:** lowercased → whitespace normalised → deduplicated (415 removed) → zero-leakage stratified split.

### 🗂️ Data Versioning & Traceability

Because training runs on Kaggle (no DVC daemon available), we use a **Git-tag + SHA-256 manifest** approach:

1. **G25AIT2016** (Data Manager) prepares the cleaned CSVs locally, commits them to the `develop` branch, and pushes a `data_manifest.json` that records SHA-256 hashes and row/class counts for every split.
2. A Git **lightweight tag** (`data-v1`, `data-v2`, `data-v3`) is applied to pin the exact commit used for each experiment.
3. The manifest is also logged as a **W&B Artifact** — every W&B training run links to the data snapshot it trained on.
4. The Kaggle training notebook pulls from `develop` at the start of each run, ensuring G25AIT2032/G25AIT2103 always train on G25AIT2016's committed data — not a locally generated copy.

This gives full reproducibility: given a W&B run ID, you can trace back to the exact data split via the artifact → Git tag → commit SHA chain.

---

## 🧪 Experiment Comparison

| Hyperparameter | v1 ★ Best | v2 | v3 |
|---|---|---|---|
| Learning Rate | 3e-5 | 2e-5 | 2e-5 |
| Epochs | 3 | 5 | 5 |
| Batch Size | 16 | 32 | 32 |
| Warmup Steps | 100 | 200 | 100 |
| Padding | dynamic | max_length | max_length |
| Early Stopping | No | Yes (p=2) | Yes (p=2) |

| Metric | v1 ★ Best | v2 | v3 |
|---|---|---|---|
| Accuracy | 0.9987 | 0.9935 | 0.9935 |
| F1 (weighted) | 0.9987 | 0.9935 | 0.9935 |
| F1 (macro) | 0.9970 | 0.9851 | 0.9851 |
| Precision | 0.9987 | 0.9935 | 0.9935 |
| Recall | 0.9987 | 0.9935 | 0.9935 |
| Val Loss | 0.0183 | 0.0292 | 0.0376 |

> **Best experiment:** **v1** achieved the highest weighted F1 score (**0.9987**) and the lowest validation loss (**0.0183**), outperforming both v2 and v3 despite using fewer epochs.
>
> Full experiment results are available in `experiment_results.csv`. Training curves and logs can be explored in the W&B dashboard: https://wandb.ai/g25ait2032-iit-jodhpur/MLOPS_Group

---

## ✅ Sanity Checks

The notebook (`group-36-mlops.ipynb`, Task 2a) performs automated sanity checks after data preparation to ensure dataset quality and prevent data leakage.

| Check | What it verifies | Result |
|---|---|---|
| Schema Validation | `text` and `label` columns exist in all splits | ✅ PASS |
| Missing Values | No `NaN` values in `text` or `label` columns | ✅ PASS |
| Label Distribution | Stratified split preserves spam ratio (12–16%) | ✅ PASS |
| Text Quality | No empty messages and reasonable average token length (5–50) | ✅ PASS |
| Data Leakage | No overlap between train, validation, and test sets | ✅ PASS |

### Split Statistics

| Split | Spam % | Empty Texts | Mean Token Length |
|---|---:|---:|---:|
| Train | 12.43% | 0 | 15.4 |
| Validation | 12.53% | 0 | 15.5 |
| Test | 12.40% | 0 | 15.4 |

### Leakage Checks

| Comparison | Overlap |
|---|---:|
| Train ∩ Validation | 0 |
| Train ∩ Test | 0 |
| Validation ∩ Test | 0 |

### Summary

- ✅ **21 / 21 sanity checks passed**
- ✅ Class distribution preserved across all splits
- ✅ No missing values detected
- ✅ No empty messages detected
- ✅ No train/validation/test leakage detected
- ✅ Dataset passed all quality validation checks

> **Result:** 🎉 All sanity checks passed — data is clean and ready for model training.

All checks print `✅ PASS` or `❌ FAIL` with a summary count. A failure aborts the run.

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/g25ait2032-prog/MLOPS_Group.git
cd MLOPS_Group

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Running Each Step

### Step 1 — Prepare Data (local, by G25AIT2016)
```bash
python src/prepare_data.py
# Outputs: data/train.csv, data/validation.csv, data/test.csv,
#          data/id2label.json, data/label2id.json, data/data_manifest.json
# Then commit + push to develop:
git add data/ && git commit -m "data(v1): prepared split" && git push origin develop
git tag data-v1 && git push origin data-v1
```

### Step 2 — Train on Kaggle (G25AIT2103)
1. Upload `notebooks/group-36-mlops.ipynb` into a new Kaggle Notebook.
2. **Do NOT re-run Task 2** — the notebook pulls data from Git (Task 1b) so you use G25AIT2016's committed split.
3. Enable GPU: **Settings → Accelerator → GPU T4 x2**.
4. Add Kaggle Secrets: `WANDB_API_KEY_gr`, `HF_TOKEN_gr`, `GITHUB_TOKEN`.
5. Set `VERSION = "v1"` in Cell 4 and run. Repeat for `"v2"` and `"v3"`.

### Step 3 — Run Inference Locally
```bash
export HF_TOKEN=your_token
export HF_MODEL=nagaananth/MLOPS_group-v2
export INPUT_TEXT="Free prize! Click now to claim."
python src/inference.py
```

### Step 4 — Docker
```bash
# Build
docker build --build-arg HF_MODEL_NAME=nagaananth/MLOPS_group-v2 \
             -t mlops_group-inference:latest .

# Run locally
docker run --rm \
  -e HF_TOKEN=your_token \
  -e INPUT_TEXT="Win a free car now!" \
  mlops_group-inference:latest

# Pull from GHCR (no build needed)
docker pull ghcr.io/g25ait2032-prog/mlops_group-inference:latest
docker run --rm \
  -e HF_TOKEN=your_token \
  -e INPUT_TEXT="Win a free car now!" \
  ghcr.io/g25ait2032-prog/mlops_group-inference:latest
```

### Step 5 — GitHub Actions Inference (manual)
1. Go to **Actions → Inference → Run workflow**.
2. Enter the text you want to classify.
3. Check the run logs for the predicted label and confidence score.

---

## 🔐 GitHub Secrets Required

| Secret | Description |
|---|---|
| `HF_TOKEN` | Hugging Face write token |
| `HF_MODEL` | HF repo ID (e.g. `nagaananth/MLOPS_group-v2`) |
| `WANDB_API_KEY` | W&B API key |
| `GITHUB_TOKEN` | Auto-provided by GitHub Actions; also added as Kaggle Secret for notebook Git pushes |

Add via: **Settings → Secrets and Variables → Actions → New repository secret**

---

## 📌 Notes

- Training is done **only on Kaggle** — GitHub Actions handles CI (linting) and inference only.
- **Data flow:** G25AIT2016 commits cleaned CSVs → Git tag pins the version → Kaggle notebook pulls via `git pull` → training uses that exact split → manifest SHA-256 confirms identity.
- Large data files (`train.csv`, `test.csv`) are committed to `develop` for reproducibility but listed in `.gitignore` on `main` to keep the default branch clean.
- Three experiment versions (v1, v2, v3) are visible in the W&B dashboard — set project visibility to **Public** before submission.
- All links must be publicly accessible at submission time.
