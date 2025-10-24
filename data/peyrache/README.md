
**Dataset URL:** https://dandiarchive.org/dandiset/000056

To download the latest version of the dataset:
```python
dandi download DANDI:000056
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/peyrache" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 2,198,184,372

**HF repo:** https://huggingface.co/datasets/eminorhan/peyrache

**Recorded area & stimulus, task, or behavior:** Recordings of head-direction (HD) neurons in the antero-dorsal thalamic nucleus and the post-subiculum of mice in various brain states.

**Paper URL:** https://www.nature.com/articles/nn.3968

```
@article{peyrache2015,
  title={Internally organized mechanisms of the head direction sense},
  author={Peyrache, Adrien and Lacroix, Marie M and Petersen, Peter C and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Nature Neuroscience},
  volume={18},
  number={4},
  pages={569--575},
  year={2015},
  publisher={Nature Publishing Group US New York}
}
```