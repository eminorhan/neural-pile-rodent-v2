[![Static Badge](https://img.shields.io/badge/🤗_datasets-neural_pile_rodent-blue)](https://huggingface.co/datasets/eminorhan/neural-pile-rodent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Spiking neural activity data recorded from rodents 

~453B uncompressed tokens of spiking neural activity data recorded from rodents (tokens=neurons x time bins). Unless otherwise noted, the data consist of spike counts in 20 ms time bins recorded from each neuron.

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
| Le Merre    | 3,903,005,243     | [dandi:001260](https://dandiarchive.org/dandiset/001260)                                                                       | [link](data/lemerre)         | mouse   | 41       |       74 |
| Peyrache    | 2,198,184,372     | [dandi:000056](https://dandiarchive.org/dandiset/000056)                                                                       | [link](data/peyrache)        | mouse   | 7        |       40 |
| Prince      | 1,921,336,974     | [dandi:001371](https://dandiarchive.org/dandiset/001371)                                                                       | [link](data/prince)          | mouse   | 7        |       66 |
| Senzai      | 1,433,511,102     | [dandi:000166](https://dandiarchive.org/dandiset/000166)                                                                       | [link](data/senzai)          | mouse   | 19       |       19 |
| Finkelstein | 1,313,786,316     | [dandi:000060](https://dandiarchive.org/dandiset/000060)                                                                       | [link](data/finkelstein)     | mouse   | 9        |       98 |
| Grosmark    | 1,158,299,763     | [dandi:000044](https://dandiarchive.org/dandiset/000044)                                                                       | [link](data/grosmark)        | rat     | 4        |        8 |
| Giocomo     | 1,083,328,404     | [dandi:000053](https://dandiarchive.org/dandiset/000053)                                                                       | [link](data/giocomo)         | mouse   | 34       |      349 |
| Steinmetz-2 | 684,731,334       | [figshare:7739750](https://figshare.com/articles/dataset/Eight-probe_Neuropixels_recordings_during_spontaneous_behaviors/7739750)| [link](data/steinmetz-2)   | mouse   | 3        |        3 |
| Jaramillo   | 581,535,289       | [dandi:000986](https://dandiarchive.org/dandiset/000986)                                                                       | [link](data/jaramillo)       | mouse   | 5        |       15 |
| Mehrotra    | 465,402,824       | [dandi:000987](https://dandiarchive.org/dandiset/000987)                                                                       | [link](data/mehrotra)        | mouse   | 3        |       14 |
| Iurilli     | 388,791,426       | [dandi:000931](https://dandiarchive.org/dandiset/000931)                                                                       | [link](data/iurilli)         | mouse   | 1        |        1 |
| Gonzalez    | 366,962,209       | [dandi:000405](https://dandiarchive.org/dandiset/000405)                                                                       | [link](data/gonzalez)        | rat     | 5        |      276 |
| Li          | 260,807,325       | [dandi:000010](https://dandiarchive.org/dandiset/000010)                                                                       | [link](data/li)              | mouse   | 23       |       99 |
| Fujisawa    | 132,563,010       | [dandi:000067](https://dandiarchive.org/dandiset/000067)                                                                       | [link](data/fujisawa)        | rat     | 3        |       10 |

**Total number of tokens:** 452,793,851,799

 The combined dataset takes up about 453 GB on disk when stored as memory-mapped `.arrow` files. The HF `datasets` library uses `.arrow` files for local caching, so you will need at least this much free disk space in order to be able to utilize it.

## Requirements
Please see the auto-generated [`requirements.txt`](requirements.txt) file.

## Creating the component datasets
The [`data`](data) directory contains all the information needed to download and preprocess the individual component datasets and push them to the HF datasets hub (quick links to the subdirectories for component datasets are provided in the Details column in the table above). You can use these as a starting point if you would like to add more datasets to the mix. Adding further `dandisets` should be particularly easy based off of the current examples. When creating the component datasets, we split long sessions (>10M tokens) into smaller equal-sized chunks of no more than 10M tokens. This makes data loading more efficient and prevents errors while creating and uploading HF datasets.

## Merging the component datasets into a single dataset
Once we have created the individual component datasets, we merge them into a single dataset with the [`merge_datasets.py`](merge_datasets.py) script. This also shuffles the combined dataset, creates a separate test split, and pushes the dataset to the HF datasets hub (please note that due to the size of the dataset, it can take several hours to push the dataset to the HF datasets hub). If you would like to add more datasets to the mix, simply add their HF dataset repository names to the `repo_list` in `merge_datasets.py`.

## Visualizing the datasets
[`visualize_dataset.py`](visualize_dataset.py) provides some basic functionality to visualize random samples from the datasets as a basic sanity check:
```python
python visualize_datasets.py --repo_name 'eminorhan/v2h' --n_examples 9
```
This will randomly sample `n_examples` examples from the corresponding dataset and visualize them as below, where *x* is the time axis (binned into 20 ms windows) and the *y* axis represents the recorded units:

![](visuals/v2h.jpg)

Users also have the option to visualize `n_examples` random examples from each component dataset by calling:
```python
python visualize_datasets.py --plot_all --n_examples 9
```
This will save the visualizations for all component datasets in a folder called `visuals` as in [here](visuals).