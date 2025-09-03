Li dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000010

Note: for this dataset, we only keep the sessions for which ephys data are available.

To download the latest version of the dataset:
```python
dandi download DANDI:000010
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/li" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 260,807,325

**HF repo:** https://huggingface.co/datasets/eminorhan/li

**Recorded area & stimulus, task, or behavior:** Recordings from the mouse anterior lateral motor cortex (ALM) during a whisker-based object location discrimination task.

**Paper URL:** https://www.nature.com/articles/nature14178

```
@article{li2015,
  title={A motor cortex circuit for motor planning and movement},
  author={Li, Nuo and Chen, Tsai-Wen and Guo, Zengcai V and Gerfen, Charles R and Svoboda, Karel},
  journal={Nature},
  volume={519},
  number={7541},
  pages={51--56},
  year={2015},
  publisher={Nature Publishing Group UK London}
}
```