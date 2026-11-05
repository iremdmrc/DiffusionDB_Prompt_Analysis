# How People Prompt AI Image Generators

**An analysis of real-world text-to-image prompts from the DiffusionDB dataset**

Final project for the *Python for Data Analysis* course.

**Students:** Tugba Irem Demirci, Ayse Sule Ekiz

---

## About the project

Generative AI tools such as Stable Diffusion let anyone create an image by typing a text prompt. But how do everyday users actually write those prompts?
In this project we use **Pandas** to clean and analyze about **110,000 real prompts** written by 500 Stable Diffusion users in August 2022, and **Matplotlib / Seaborn** to visualize the results.

### Research questions

1. **Styles and artists:** Which artistic styles, mediums and artist names appear most often in prompts, and how concentrated is their use among a small number of popular terms?
2. **Prompt revision:** How do users revise their prompts within a session? Do prompts become longer or more style-specific over repeated generations by the same user?
3. **Generation settings:** How are settings such as guidance scale, step count and image size distributed, and do they relate to prompt length or complexity?

### Key findings so far

- **Quality boosters beat art styles.** Generic phrases such as *"trending on artstation"*, *"highly detailed"* and *"4k / 8k"* appear in 53% of prompts, more often than any medium (47%) or art style (38%).
- **Artist names are highly concentrated.** 27% of prompts name an artist. Greg Rutkowski alone accounts for 13% of all artist mentions, and the top 10 artists for 43%. Half of all artist names appear only once.
- **Prompts grow slowly during a session.** Across a session, prompts get slightly longer (20 to 22 words on average) and more style-specific. 61% of changes are small edits of the same idea, and most edits keep the same style keywords while changing the subject.
- **Most people keep the default settings,** but users who write longer prompts change them much more often. 73% of short prompts (10 words or fewer) use all defaults, compared with 14% of long prompts (41 to 60 words). This is an association, not a cause.

---

## Dataset

| | |
|---|---|
| **Name** | DiffusionDB (2M subset, metadata table) |
| **Source** | Polo Club of Data Science, Georgia Institute of Technology |
| **Link** | https://huggingface.co/datasets/poloclub/diffusiondb |
| **License** | CC0 1.0 (public domain) |
| **Full table** | 2,000,000 rows x 13 columns (`metadata.parquet`, 185 MB) |
| **Our sample** | 110,698 rows x 13 columns (`data/diffusiondb_sample.parquet`, 16 MB) |

**How the sample was made** (see [`make_sample.py`](make_sample.py)): we randomly selected **500 users** (`random_state=42`) and kept **all** of their generations, so that each user's sessions stay complete for Research Question 2.
Rows without a usable user ID were sampled at a 5% rate.
The sample file is already in this repository, so you do **not** need to download the full dataset.

---

## Repository structure

```
.
├── DiffusionDB_Prompt_Analysis.ipynb   # main notebook (the project submission)
├── data/
│   └── diffusiondb_sample.parquet      # ~110k-row sample used by the notebook
├── make_sample.py                      # script that created the sample from the full dataset
├── requirements.txt                    # Python packages needed
└── README.md
```

## Notebook sections

| Section | Content | Status |
|---|---|---|
| 1 | Project introduction | Done |
| 2 | Loading the dataset | Done |
| 3 | Understanding the dataset | Done |
| 4 | Data cleaning: missing values, duplicates, data types, inconsistent text and artist names, NSFW filter, outliers | Done |
| 5 | Exploratory data analysis with Pandas (Q1-Q3) | Done |
| 6 | Data visualization | In progress (Ayse Sule Ekiz) |
| 7-10 | Interpretation, answers, limitations, conclusion | To do |
| 11 | References | Done (add visualization sources) |

---

## How to run the notebook

### 1. Install the tools
- **Python 3.10 or newer**: https://www.python.org/downloads/ (on Windows, tick *"Add python.exe to PATH"* during setup)
- **Visual Studio Code**: https://code.visualstudio.com/, with the **Python** and **Jupyter** extensions (from the Extensions tab)

### 2. Get the project
```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 3. Install the Python packages
```bash
python -m pip install -r requirements.txt
```

### 4. Open and run
Open the project folder in VS Code, open `DiffusionDB_Prompt_Analysis.ipynb`, choose your Python installation as the kernel (top right), and click **Run All**.
The whole notebook runs in under a minute.

> Prefer the classic browser interface? Run `python -m pip install notebook` and then `python -m notebook`.

### (Optional) Re-create the sample from the full dataset
```bash
python make_sample.py
```
This downloads the full `metadata.parquet` (185 MB) from Hugging Face and writes `data/diffusiondb_sample.parquet`.

---

## Tools and libraries

Python, pandas, NumPy, PyArrow (to read Parquet files), Matplotlib, seaborn, Jupyter.

## References

1. Wang, Z. J., Montoya, E., Munechika, D., Yang, H., Hoover, B., & Chau, D. H. (2022). *DiffusionDB: A Large-scale Prompt Gallery Dataset for Text-to-Image Generative Models.* arXiv:2210.14896. https://arxiv.org/abs/2210.14896
2. DiffusionDB on Hugging Face: https://huggingface.co/datasets/poloclub/diffusiondb
3. DiffusionDB GitHub repository: https://github.com/poloclub/diffusiondb
4. pandas documentation: https://pandas.pydata.org/docs/
