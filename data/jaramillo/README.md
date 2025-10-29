
**Dataset URL:** https://dandiarchive.org/dandiset/000986

To download the latest version of the dataset:
```python
dandi download DANDI:000986
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/jaramillo" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 581,535,289

**HF repo:** https://huggingface.co/datasets/eminorhan/jaramillo

**Recorded area & stimulus, task, or behavior:** Recordings from the auditory cortex of behaving mice during passive tone presentation.

**Paper URL:** https://www.biorxiv.org/content/10.1101/2024.04.04.588209v2

```
@article{papadopoulos2024,
  title={Modulation of metastable ensemble dynamics explains optimal coding at moderate arousal in auditory cortex},
  author={Papadopoulos, Lia and Jo, Suhyun and Zumwalt, Kevin and Wehr, Michael and McCormick, David A and Mazzucato, Luca},
  journal={bioRxiv},
  year={2024}
}
```