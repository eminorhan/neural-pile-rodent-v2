Steinmetz-2 dataset. 

**Dataset URL:** https://figshare.com/articles/dataset/Eight-probe_Neuropixels_recordings_during_spontaneous_behaviors/7739750

The data files were downloaded manually from the above URL. Put the data under a new `data` folder with separate subfolders for each of the three subjects. Then, to process the data and push it to the HF Hub as a separate dataset repository, run *e.g.*:
```python
python create_dataset.py --hf_repo_name "eminorhan/steinmetz-2" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 1,830,825,994

**HF repo:** https://huggingface.co/datasets/eminorhan/steinmetz-2

**Recorded area & stimulus, task, or behavior:** Brain-wide recordings from mice with eight Neuropixels probes during spontaneous behaviors.

**Paper URL:** https://www.science.org/doi/10.1126/science.aav7893

```
@article{stringer2019,
  title={Spontaneous behaviors drive multidimensional, brainwide activity},
  author={Stringer, Carsen and Pachitariu, Marius and Steinmetz, Nicholas and Reddy, Charu Bai and Carandini, Matteo and Harris, Kenneth D},
  journal={Science},
  volume={364},
  number={6437},
  pages={eaav7893},
  year={2019},
  publisher={American Association for the Advancement of Science}
}
```