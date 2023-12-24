# rct-model-evaluation

Adapting randomized controlled trials (RCT) for model evaluation to establish causation

## Setup

1. Install prerequisites

```bash
pip install -r src/requirements.txt
```

## Data preparation using contrast sets

1. IMDB - download original and contrast set from here https://github.com/allenai/contrast-sets/tree/main/IMDb/data

```bash
python src/preprocess_rct_imdb.py tests/sample_data/imdb_original.tsv tests/sample_data/imdb_contrast.tsv temp/rct_imdb.json
```