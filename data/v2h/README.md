Vision2Hippocampus dataset from the Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/000690

To download the latest version of the dataset:
```python
dandi download DANDI:000690
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/v2h" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 24,600,171,007

**HF repo:** https://huggingface.co/datasets/eminorhan/v2h

**Recorded area & stimulus, task, or behavior:** Simultaneous recordings from multiple cortical and subcortical areas in mice in response to a variety of visual stimuli.

**Paper URL:** N/A

```
@dataset{v2h2025,
  author    = {Mehta, Mayank R and Purandare, Chinmay and Jha, Siddharth and Lecoq, Jérôme and Durand, Séverine and Gillis, Ryan and Belski, Hannah and Bawany, Ahad and Carlson, Mikayla and Peene, Carter and Wilkes, Josh and Johnson, Tye and Naidoo, Robyn and Suarez, Lucas and Han, Warren and Amaya, Avalon and Nguyen, Katrina and Ouellette, Ben and Swapp, Jackie and Williford, Ali},
  title     = {Allen Institute Openscope - Vision2Hippocampus project},
  year      = {2025},
  publisher = {DANDI Archive},
  doi       = {10.48324/dandi.000690/0.250326.0015},
  url       = {https://doi.org/10.48324/dandi.000690/0.250326.0015},
  version   = {0.250326.0015},
  type      = {Data set}
}
```