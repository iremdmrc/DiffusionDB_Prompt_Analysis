"""
make_sample.py
--------------
Creates the ~100,000-row sample of the DiffusionDB 2M metadata table that the
notebook uses (data/diffusiondb_sample.parquet).

You do NOT need to run this to use the notebook - the sample file is already in
the repository. It is included so anyone can see exactly how the sample was made
and reproduce it.

How the sample is built
  1. Download the full metadata table (metadata.parquet, ~185 MB, 2,000,000 rows)
     from Hugging Face.
  2. Randomly choose 500 real users (random_state=42) and keep ALL of their rows.
     We sample users instead of single rows because Research Question 2 studies
     how a person revises prompts within a session; a row-level sample would
     break sessions into disconnected pieces.
  3. Rows that have no real user ID ("deleted_acount" or missing) cannot be
     grouped into users, so we take a simple 5% random sample of them. This keeps
     the same data-quality problems in the sample as in the full table.

Usage
  python make_sample.py                     # downloads metadata.parquet first
  python make_sample.py path/to/metadata.parquet
"""

import sys
import urllib.request
from pathlib import Path

import pandas as pd

URL = "https://huggingface.co/datasets/poloclub/diffusiondb/resolve/main/metadata.parquet"
N_USERS = 500
NO_USER_FRACTION = 0.05
SEED = 42
OUT = Path("data") / "diffusiondb_sample.parquet"


def main():
    if len(sys.argv) > 1:
        full_path = Path(sys.argv[1])
    else:
        full_path = Path("metadata.parquet")
        if not full_path.exists():
            print("Downloading metadata.parquet (~185 MB)...")
            urllib.request.urlretrieve(URL, full_path)

    full = pd.read_parquet(full_path)
    print("Full table:", full.shape)

    no_user = full["user_name"].isna() | (full["user_name"] == "deleted_acount")
    real_users = full.loc[~no_user, "user_name"].drop_duplicates()
    chosen = real_users.sample(N_USERS, random_state=SEED)

    part_users = full[full["user_name"].isin(chosen)]
    part_no_user = full[no_user].sample(frac=NO_USER_FRACTION, random_state=SEED)

    sample = (
        pd.concat([part_users, part_no_user])
        .sample(frac=1, random_state=SEED)  # shuffle row order
        .reset_index(drop=True)
    )

    OUT.parent.mkdir(exist_ok=True)
    sample.to_parquet(OUT, index=False)
    print("Sample saved to", OUT, sample.shape)


if __name__ == "__main__":
    main()
