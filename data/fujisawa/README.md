
**Dataset URL:** https://dandiarchive.org/dandiset/000067

To download the latest version of the dataset:
```python
dandi download DANDI:000067
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/fujisawa" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 132,563,010

**HF repo:** https://huggingface.co/datasets/eminorhan/fujisawa

**Recorded area & stimulus, task, or behavior:** Recordings from the medial prefrontal cortex of rats during a working memory task.

**Paper URL:** https://www.nature.com/articles/nn.2134

```
@article{fujisawa2008,
  title={Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex},
  author={Fujisawa, Shigeyoshi and Amarasingham, Asohan and Harrison, Matthew T and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Nature Neuroscience},
  volume={11},
  number={7},
  pages={823--833},
  year={2008},
  publisher={Nature Publishing Group US New York}
}
```