while IFS= read -r path; do
  dandi download --preserve-tree "dandi://dandi/000409/$path"
done < processed_paths.txt