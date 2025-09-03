Steinmetz dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000017

To download the latest version of the dataset:
```python
dandi download DANDI:000017
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/steinmetz" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 7,881,422,592

**HF repo:** https://huggingface.co/datasets/eminorhan/steinmetz

**Recorded area & stimulus, task, or behavior:** Brain-wide recordings from mice during a perceptual decision-making task.

**Paper URL:** https://www.nature.com/articles/s41586-019-1787-x

```
@article{steinmetz2019,
  title={Distributed coding of choice, action and engagement across the mouse brain},
  author={Steinmetz, Nicholas A and Zatka-Haas, Peter and Carandini, Matteo and Harris, Kenneth D},
  journal={Nature},
  volume={576},
  number={7786},
  pages={266--273},
  year={2019},
  publisher={Nature Publishing Group UK London}
}
```