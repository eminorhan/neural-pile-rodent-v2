Gonzalez dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000405

To download the latest version of the dataset:
```python
dandi download DANDI:000405
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/gonzalez" --token_count_limit 10_000_000
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, and `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks).

**Token count:** 366,962,209

**HF repo:** https://huggingface.co/datasets/eminorhan/gonzalez

**Recorded area & stimulus, task, or behavior:** Recordings from rat parahippocampal cortex during a memory-guided spatial navigation task.

**Paper URL:** https://elifesciences.org/articles/85646

```
@article{gonzalez2024,
  title={Parahippocampal neurons encode task-relevant information for goal-directed navigation},
  author={Gonzalez, Alexander and Giocomo, Lisa M},
  journal={eLife},
  volume={12},
  pages={RP85646},
  year={2024},
  publisher={eLife Sciences Publications Limited}
}
```