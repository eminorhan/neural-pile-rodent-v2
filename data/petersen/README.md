Petersen dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000059

To download the latest version of the dataset:
```python
dandi download DANDI:000059
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/petersen" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 15,510,368,376

**HF repo:** https://huggingface.co/datasets/eminorhan/petersen

**Recorded area & stimulus, task, or behavior:** Recordings from rat hippocampus during a spatial navigation task (includes recordings made when medial septum was cooled).

**Paper URL:** https://www.cell.com/neuron/fulltext/S0896-6273(20)30392-5

```
@article{petersen2020,
  title={Cooling of medial septum reveals theta phase lag coordination of hippocampal cell assemblies},
  author={Petersen, Peter Christian and Buzs{\'a}ki, Gy{\"o}rgy},
  journal={Neuron},
  volume={107},
  number={4},
  pages={731--744},
  year={2020},
  publisher={Elsevier}
}
```