Mehrotra dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000987

To download the latest version of the dataset:
```python
dandi download DANDI:000987
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/mehrotra" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 465,402,824

**HF repo:** https://huggingface.co/datasets/eminorhan/mehrotra

**Recorded area & stimulus, task, or behavior:** Recordings from mouse retrosplenial cortex during sleep and open field exploration.

**Paper URL:** https://doi.org/10.1016/j.cub.2024.05.048

```
@article{mehrotra2024,
  title={Hyperpolarization-activated currents drive neuronal activation sequences in sleep},
  author={Mehrotra, Dhruv and Levenstein, Daniel and Duszkiewicz, Adrian J and Carrasco, Sofia Skromne and Booker, Sam A and Kwiatkowska, Angelika and Peyrache, Adrien},
  journal={Current Biology},
  volume={34},
  number={14},
  pages={3043--3054},
  year={2024},
  publisher={Elsevier}
}
```