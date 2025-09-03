[![Static Badge](https://img.shields.io/badge/🤗_datasets-neural_pile_rodent-blue)](https://huggingface.co/datasets/eminorhan/neural-pile-rodent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Spiking neural activity data recorded from rodents 

~441B uncompressed tokens of spiking neural activity data recorded from rodents (tokens=neurons x time bins). Unless otherwise noted, the data consist of spike counts in 20 ms time bins recorded from each neuron.

This repository contains the code and instructions for building the dataset from scratch. The actual final dataset is hosted at [this](https://huggingface.co/datasets/eminorhan/neural-pile-rodent) public HF repository.

The current component datasets and token counts per dataset are as follows:

| Name        | Tokens            | Source                                                                                                                      | Details                      | Species | Subjects | Sessions |
| :---------- | ----------------: | :-------------------------------------------------------------------------------------------------------------------------- | :---------------------------|:--------|---------:| -------: |
| VBN         | 153,877,057,200   | [dandi:000713](https://dandiarchive.org/dandiset/000713)                                                                       | [link](data/vbn)             | mouse   | 81       |      153 |
| IBL         | 69,147,814,139    | [dandi:000409](https://dandiarchive.org/dandiset/000409)                                                                       | [link](data/ibl)             | mouse   | 115      |      347 |
| SHIELD      | 61,890,305,241    | [dandi:001051](https://dandiarchive.org/dandiset/001051)                                                                       | [link](data/shield)          | mouse   | 27       |       99 |
| VCN         | 36,681,686,005    | [dandi:000021](https://dandiarchive.org/dandiset/000021)                                                                       | [link](data/vcn)             | mouse   | 32       |       32 |
| VCN-2       | 30,600,253,445    | [dandi:000022](https://dandiarchive.org/dandiset/000022)                                                                       | [link](data/vcn-2)           | mouse   | 26       |       26 |
| V2H         | 24,600,171,007    | [dandi:000690](https://dandiarchive.org/dandiset/000690)                                                                       | [link](data/v2h)             | mouse   | 25       |       25 |
| Petersen    | 15,510,368,376    | [dandi:000059](https://dandiarchive.org/dandiset/000059)                                                                       | [link](data/petersen)        | rat     | 5        |       24 |
| Oddball     | 14,653,641,118    | [dandi:000253](https://dandiarchive.org/dandiset/000253)                                                                       | [link](data/oddball)         | mouse   | 14       |       14 |
| Illusion    | 13,246,412,456    | [dandi:000248](https://dandiarchive.org/dandiset/000248)                                                                       | [link](data/illusion)        | mouse   | 12       |       12 |
| Huszar      | 8,812,474,629     | [dandi:000552](https://dandiarchive.org/dandiset/000552)                                                                       | [link](data/huszar)          | mouse   | 17       |       65 |
| Steinmetz   | 7,881,422,592     | [dandi:000017](https://dandiarchive.org/dandiset/000017)                                                                       | [link](data/steinmetz)       | mouse   | 10       |       39 |
| Finkelstein | 1,313,786,316     | [dandi:000060](https://dandiarchive.org/dandiset/000060)                                                                       | [link](data/finkelstein)     | mouse   | 9        |       98 |
| Giocomo     | 1,083,328,404     | [dandi:000053](https://dandiarchive.org/dandiset/000053)                                                                       | [link](data/giocomo)         | mouse   | 34       |      349 |
| Steinmetz-2 | 684,731,334       | [figshare:7739750](https://figshare.com/articles/dataset/Eight-probe_Neuropixels_recordings_during_spontaneous_behaviors/7739750)| [link](data/steinmetz-2)     | mouse   | 3        |        3 |
| Mehrotra    | 465,402,824       | [dandi:000987](https://dandiarchive.org/dandiset/000987)                                                                       | [link](data/mehrotra)        | mouse   | 3        |       14 |
| Iurilli     | 388,791,426       | [dandi:000931](https://dandiarchive.org/dandiset/000931)                                                                       | [link](data/iurilli)         | mouse   | 1        |        1 |
| Gonzalez    | 366,962,209       | [dandi:000405](https://dandiarchive.org/dandiset/000405)                                                                       | [link](data/gonzalez)        | rat     | 5        |      276 |
| Li          | 260,807,325       | [dandi:000010](https://dandiarchive.org/dandiset/000010)                                                                       | [link](data/li)              | mouse   | 23       |       99 |

**Total number of tokens:** 441,465,416,046

 The combined dataset takes up about 47 GB when stored as `.parquet` files and roughly 443 GB when stored as memory-mapped `.arrow` files (see [this](https://stackoverflow.com/a/56481636) for an explanation of the differences between these file formats). The HF `datasets` library uses `.arrow` files for local caching, so you will need at least this much free disk space in order to be able to utilize it.

## Requirements
Please see the auto-generated [`requirements.txt`](requirements.txt) file.

## Creating the component datasets
The [`data`](data) directory contains all the information needed to download and preprocess the individual component datasets and push them to the HF datasets hub (quick links to the subdirectories for component datasets are provided in the Details column in the table above). You can use these as a starting point if you would like to add more datasets to the mix. Adding further `dandisets` should be particularly easy based off of the current examples. When creating the component datasets, we split long sessions (>10M tokens) into smaller equal-sized chunks of no more than 10M tokens. This makes data loading more efficient and prevents errors while creating and uploading HF datasets.

## Merging the component datasets into a single dataset
Once we have created the individual component datasets, we merge them into a single dataset with the [`merge_datasets.py`](merge_datasets.py) script. This also shuffles the combined dataset, creates a separate test split, and pushes the dataset to the HF datasets hub. If you would like to add more datasets to the mix, simply add their HF dataset repository names to the `repo_list` in `merge_datasets.py`.

### Note:
Running `merge_datasets.py` successfully requires a patch in the `huggingface_hub` library (as of version `0.29.1`; I haven't tested newer versions). The HF `datasets` library doesn't do retries while loading datasets from the hub (`load_dataset`) or when pushing them to the hub (`push_to_hub`). This almost always results in connection errors for large datasets in my experience, aborting the loading or pushing of the dataset. The patch involves adding a "retry" functionality to `huggingface_hub`'s default session backend factory. Specifically, you need to update the `_default_backend_factory()` function in `huggingface_hub/utils/_http.py` with:
```python
from requests.adapters import HTTPAdapter, Retry

...

def _default_backend_factory() -> requests.Session:
    session = requests.Session()
    retries = Retry(total=20, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    if constants.HF_HUB_OFFLINE:
        session.mount("http://", OfflineAdapter(max_retries=retries))
        session.mount("https://", OfflineAdapter(max_retries=retries))
    else:
        session.mount("http://", UniqueRequestIdAdapter(max_retries=retries))
        session.mount("https://", UniqueRequestIdAdapter(max_retries=retries))
    return session
```  
or something along these lines (you can play with the `Retry` settings). This will prevent the premature termination of the job when faced with connection issues. 

## Visualizing the datasets
[`visualize_dataset.py`](visualize_dataset.py) provides some basic functionality to visualize random samples from the datasets:
```python
python visualize_datasets.py --repo_name 'eminorhan/vbn' --n_examples 6
```
This will randomly sample `n_examples` examples from the corresponding dataset and visualize them as below, where *x* is the time axis (binned into 20 ms windows) and the *y* axis represents the recorded units:

![](assets/vbn.jpg)
