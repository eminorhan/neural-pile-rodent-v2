Huszar dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000552

Note: for this dataset, we only keep the sessions for which ephys data are available.

To download the latest version of the dataset:
```python
dandi download DANDI:000552
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/huszar" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 8,812,474,629

**HF repo:** https://huggingface.co/datasets/eminorhan/huszar

**Recorded area & stimulus, task, or behavior:** Recordings from the CA1 region of mouse hippocampus during a spatial alternation task in a figure-eight maze.

**Paper URL:** https://www.nature.com/articles/s41593-022-01138-x
```
@article{huszar2022,
  title={Preconfigured dynamics in the hippocampus are guided by embryonic birthdate and rate of neurogenesis},
  author={Husz{\'a}r, Roman and Zhang, Yunchang and Blockus, Heike and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Nature Neuroscience},
  volume={25},
  number={9},
  pages={1201--1212},
  year={2022},
  publisher={Nature Publishing Group US New York}
}
```