
**Dataset URL:** https://dandiarchive.org/dandiset/001371

To download the latest version of the dataset:
```python
dandi download DANDI:001371
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/prince" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,921,336,974

**HF repo:** https://huggingface.co/datasets/eminorhan/prince

**Recorded area & stimulus, task, or behavior:** Recordings from the hippocampal CA1 region and the medial prefrontal cortex in mice during a virtual reality spatial navigation task.

**Paper URL:** https://www.nature.com/articles/s41467-025-60122-8

```
@article{prince2025,
  title={New information triggers prospective codes to adapt for flexible navigation},
  author={Prince, Stephanie M and Cushing, Sarah Danielle and Yassine, Teema A and Katragadda, Navya and Roberts, Tyler C and Singer, Annabelle C},
  journal={Nature Communications},
  volume={16},
  number={1},
  pages={4822},
  year={2025},
  publisher={Nature Publishing Group UK London}
}
```