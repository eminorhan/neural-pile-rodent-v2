Visual Behavior - Neuropixels dataset from Allen Institute. 

**Dataset URL:** https://dandiarchive.org/dandiset/000713

To download the dataset:
```python
python download_dataset.py ecephys_sessions.csv
```
where the `ecephys_sessions.csv` file contains the session ids we want to download.

To process the data and push it to the HF Hub as a separate dataset repository:
```python
python create_dataset.py --hf_repo_name "eminorhan/vbn" --token_count_limit 10_000_000 --bin_size 0.02
```
where `hf_repo_name` is the HF dataset repository name where the processed data will be pushed to, `token_count_limit` is the maximum token count per dataset row (sessions with larger token counts than this will be split into smaller chunks), and `bin_size` is bin size in seconds for aggregating spike counts (default: 20 ms).

**Session count:** 153

**Token count:** 153,877,057,200

**HF repo:** https://huggingface.co/datasets/eminorhan/vbn

**Recorded area & stimulus, task, or behavior:** Recordings from mouse visual cortical areas including VISp, VISl, VISal, VISrl, VISam, and VISpm (up to 6 probes at a time). Multiple subcortical areas are also typically recorded, including visual thalamic areas LGd and LP as well as units in the hippocampus and midbrain. The task is a visual change detection task.

**Paper URL:** https://portal.brain-map.org/circuits-behavior/visual-behavior-neuropixels

```
@techreport{allen2022,
  author      = {{Allen Institute for Brain Science}},
  title       = {Allen Brain Observatory: Visual Behavior Neuropixels - Technical Whitepaper},
  institution = {Allen Institute for Brain Science},
  year        = {2022},
  url         = {https://portal.brain-map.org/circuits-behavior/visual-behavior-neuropixels},
  note        = {Accessed: 2025-04-28} 
}
```