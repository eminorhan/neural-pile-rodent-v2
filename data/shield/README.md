SHIELD dataset from the Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/001051

To download the latest version of the dataset:
```python
dandi download DANDI:001051
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/shield" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 61,890,305,241

**HF repo:** https://huggingface.co/datasets/eminorhan/shield

**Recorded area & stimulus, task, or behavior:** Simultaneous recordings from multiple cortical and subcortical areas in mice during a visual change detection task closely related to the VBN task.

**Paper URL:** https://www.cell.com/neuron/abstract/S0896-6273(24)00450-1

```
@article{shield2024,
  title={SHIELD: Skull-shaped hemispheric implants enabling large-scale electrophysiology datasets in the mouse brain},
  author={Bennett, Corbett and Ouellette, Ben and Ramirez, Tamina K and Cahoon, Alex and Cabasco, Hannah and Browning, Yoni and Lakunina, Anna and Lynch, Galen F and McBride, Ethan G and Belski, Hannah and others},
  journal={Neuron},
  volume={112},
  number={17},
  pages={2869--2885},
  year={2024},
  publisher={Elsevier}
}
```
