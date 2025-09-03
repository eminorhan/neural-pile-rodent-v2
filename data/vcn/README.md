Visual Coding Neuropixels (VCN) dataset from the Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/000021

To download the latest version of the dataset:
```python
dandi download DANDI:000021
```

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/vcn" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Token count:** 36,681,686,005

**HF repo:** https://huggingface.co/datasets/eminorhan/vcn

**Recorded area & stimulus, task, or behavior:** Simultaneous recordings from multiple cortical and subcortical areas in mice in response to a variety of visual stimuli.

**Paper URL:** https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels

```
@techreport{allen2019,
  author      = {{Allen Institute for Brain Science}},
  title       = {Allen Brain Observatory: Neuropixels Visual Coding - Technical Whitepaper},
  institution = {Allen Institute for Brain Science},
  year        = {2019},
  url         = {https://portal.brain-map.org/circuits-behavior/visual-coding-neuropixels},
  note        = {Accessed: 2025-04-28} 
}
```