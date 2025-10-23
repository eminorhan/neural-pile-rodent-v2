
**Dataset URL:** https://dandiarchive.org/dandiset/001260

To download the latest version of the dataset:
```python
dandi download DANDI:001260
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/lemerre" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 3,899,259,525

**HF repo:** https://huggingface.co/datasets/eminorhan/lemerre

**Recorded area & stimulus, task, or behavior:** Brain-wide high-density extracellular recordings (Neuropixels) in head-fixed mice during distinct passive listening and auditory behavioral tasks.

**Paper URL:** https://www.biorxiv.org/content/10.1101/2024.11.06.622308v2

```
@article{lemerre2024,
  title={A Prefrontal Cortex Map based on Single Neuron Activity},
  author={Merre, Pierre Le and Heining, Katharina and Slashcheva, Marina and Jung, Felix and Moysiadou, Eleni and Guyon, Nicolas and Yahya, Ram and Park, Hyunsoo and Wernstal, Fredrik and Carl{\'e}n, Marie},
  journal={bioRxiv},
  pages={2024--11},
  year={2024},
  publisher={Cold Spring Harbor Laboratory}
}

```