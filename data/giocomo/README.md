Giocomo dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000053

To download the latest version of the dataset:
```python
dandi download DANDI:000053
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/giocomo" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,083,328,404

**HF repo:** https://huggingface.co/datasets/eminorhan/giocomo

**Recorded area & stimulus, task, or behavior:** Tetrode recordings from medial entorhinal cortex in mice during open field navigation and neuropixels recordings from medial entorhinal cortex in mice during navigation down a virtual linear track.

**Paper URL:** https://www.nature.com/articles/s41467-021-20936-8

```
@article{mallory2021,
  title={Mouse entorhinal cortex encodes a diverse repertoire of self-motion signals},
  author={Mallory, Caitlin S and Hardcastle, Kiah and Campbell, Malcolm G and Attinger, Alexander and Low, Isabel IC and Raymond, Jennifer L and Giocomo, Lisa M},
  journal={Nature Communications},
  volume={12},
  number={1},
  pages={671},
  year={2021},
  publisher={Nature Publishing Group UK London}
}
```