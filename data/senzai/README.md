
**Dataset URL:** https://dandiarchive.org/dandiset/000166

To download the latest version of the dataset:
```python
dandi download DANDI:000166
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/senzai" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,433,511,102

**HF repo:** https://huggingface.co/datasets/eminorhan/senzai

**Recorded area & stimulus, task, or behavior:** Recordings from the primary visual cortex of freely behaving mice.

**Paper URL:** https://www.sciencedirect.com/science/article/pii/S0896627318310857

```
@article{senzai2019,
  title={Layer-specific physiological features and interlaminar interactions in the primary visual cortex of the mouse},
  author={Senzai, Yuta and Fernandez-Ruiz, Antonio and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Neuron},
  volume={101},
  number={3},
  pages={500--513},
  year={2019},
  publisher={Elsevier}
}
```