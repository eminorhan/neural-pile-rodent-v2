Iurilli dataset. 

**Dataset URL:** https://dandiarchive.org/dandiset/000931

To download the latest version of the dataset:
```python
dandi download DANDI:000931
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/iurilli" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 388,791,426

**HF repo:** https://huggingface.co/datasets/eminorhan/iurilli

**Recorded area & stimulus, task, or behavior:** Recordings from mouse piriform cortex in response to odors under different inhalation speeds.

**Paper URL:** https://www.cell.com/cell-reports/fulltext/S2211-1247(24)00341-3

```
@article{dehaqani2024,
  title={A mechanosensory feedback that uncouples external and self-generated sensory responses in the olfactory cortex},
  author={Dehaqani, Alireza A and Michelon, Filippo and Patella, Paola and Petrucco, Luigi and Piasini, Eugenio and Iurilli, Giuliano},
  journal={Cell Reports},
  volume={43},
  number={4},
  year={2024},
  publisher={Elsevier}
}
```