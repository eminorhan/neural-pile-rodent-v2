Oddball dataset from the Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/000253

To download the latest version of the dataset:
```python
dandi download DANDI:000253
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/oddball" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 14,653,641,118

**HF repo:** https://huggingface.co/datasets/eminorhan/oddball

**Recorded area & stimulus, task, or behavior:** Simultaneous recordings from multiple cortical areas in mice in response to simple visual stimuli.

**Paper URL:** N/A

```
@dataset{oddball2024,
  author    = {Westerberg, Jake and Durand, Severine and Cabasco, Hannah and Belski, Hannah and Loeffler, Henry and Bawany, Ahad and Peene, R. Carter and Han, Warren and Nguyen, Katrina and Ha, Vivian and Johnson, Tye and Grasso, Conor and Hardcastle, Ben and Young, Ahrial and Swapp, Jackie and Gillis, Ryan and Ouellette, Ben and Caldejon, Shiella and Williford, Ali and Groblewski, A. Peter and Olsen, Shawn and Kiselycznyk, Carly and Lecoq, Jerome and Maier, Alex and Bastos, Andre},
  title     = {Allen Institute Openscope - Global/Local Oddball project},
  year      = {2024},
  publisher = {DANDI archive},
  doi       = {10.48324/dandi.000253/0.240923.1441},
  url       = {https://doi.org/10.48324/dandi.000253/0.240923.1441},
  version   = {0.240923.1441},
  type      = {Data set}
}
```