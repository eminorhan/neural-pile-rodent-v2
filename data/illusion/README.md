Openscope Illusion project dataset from the Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/000248

To download:
```python
dandi download DANDI:000248
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/illusion" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 13,246,412,456

**HF repo:** https://huggingface.co/datasets/eminorhan/illusion

**Recorded area & stimulus, task, or behavior:** Simultaneous recordings from multiple visual cortical areas (V1, LM, RL, AL, PM, AM) in mice in response to illusory contour stimuli.

**Paper URL:** https://www.biorxiv.org/content/10.1101/2023.06.05.543698v1

```
@article{shin2023,
  title={Recurrent pattern completion drives the neocortical representation of sensory inference},
  author={Shin, Hyeyoung and Ogando, Mora B and Abdeladim, Lamiae and Durand, Severine and Belski, Hannah and Cabasco, Hannah and Loefler, Henry and Bawany, Ahad and Hardcastle, Ben and Wilkes, Josh and others},
  journal={bioRxiv},
  year={2023}
}
```