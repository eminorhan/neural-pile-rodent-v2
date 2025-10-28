
**Dataset URL:** https://dandiarchive.org/dandiset/000044

To download the latest version of the dataset:
```python
dandi download DANDI:000044
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/grosmark" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,158,299,763

**HF repo:** https://huggingface.co/datasets/eminorhan/grosmark

**Recorded area & stimulus, task, or behavior:** Recordings from the hippocampal CA1 region in rats during and after the exploration of novel mazes.

**Paper URL:** https://www.science.org/doi/10.1126/science.aad1935

```
@article{grosmark2016,
  title={Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences},
  author={Grosmark, Andres D and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Science},
  volume={351},
  number={6280},
  pages={1440--1443},
  year={2016},
  publisher={American Association for the Advancement of Science}
}
```