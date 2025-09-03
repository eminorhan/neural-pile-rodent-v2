Finkelstein dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000060

To download the latest version of the dataset:
```python
dandi download DANDI:000060
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/finkelstein" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,313,786,316

**HF repo:** https://huggingface.co/datasets/eminorhan/finkelstein

**Recorded area & stimulus, task, or behavior:** Recordings from the anterior lateral motor cortex and vibrissal sensory cortex of mice trained to detect optogenetic stimulation of vibrissal sensory cortex.

**Paper URL:** https://www.nature.com/articles/s41593-021-00840-6

```
@article{finkelstein2021,
  title={Attractor dynamics gate cortical information flow during decision-making},
  author={Finkelstein, Arseny and Fontolan, Lorenzo and Economo, Michael N and Li, Nuo and Romani, Sandro and Svoboda, Karel},
  journal={Nature Neuroscience},
  volume={24},
  number={6},
  pages={843--850},
  year={2021},
  publisher={Nature Publishing Group US New York}
}
```