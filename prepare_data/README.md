## Prepare CuRe Dataset
---

The CuRe dataset is carefully constructed from WikiMedia's categorical structure to preserve hierarchical relationships between cultural taxonomy. This means CuRe has a coarse-to-fine categorical structure of {supercategories &rarr; categories &rarr; regional variants} across geographical regions, which are assumed to be a proxy for global cultures. Each individual category typically has 10 regional variants, each of which is a specific named entity. A list of the six supercategories and their corresponding sub categories are given below:
1. [Architecture](cure_dataset_csv/architecture.csv): Bridge, Fortification, House, Monument and memorial, Religious building
2. [Art](cure_dataset_csv/art.csv): Statue, Pottery, Oil painting, Bust, Fresco
3. [Celebrations](cure_dataset_csv/celebrations.csv): Christmas food, New Year celebration, Harvest festival, Spring festival, Carnival
4. [Fashion](cure_dataset_csv/fashion.csv): Embroidery, Hat, Jewellery, Traditional clothing
5. [Food](cure_dataset_csv/food.csv): Dumplings, Flatbread, Fried Dough, Noodle Dish, Rice Dish
6. [People](cure_dataset_csv/people.csv): Politician, Musician, Writer, Sportsperson, Actor, Activist, Filmmaker

### Download WikiMedia images (ground-truth)

Download ground truth (GT) images for any category from Wikimedia with [commons-downloader](https://git.sr.ht/~nytpu/commons-downloader). Run on an entire CuRe category with `python download_wikimedia_images.py --category=art`. Images are saved by default in `gt_images/`.

### Clean and preprocess Wikimedia Images 

The Wikimedia image distribution across categories is long-tail. Currently, we manually select a subset of four representative GT images per cultural artifact with the help of ipyplot in [select_gt_data.ipynb](ground_truth_data/select_gt_data.ipynb). Finally, we clean the four selected GT images (crop / zoom) in [crop_and_zoom_image.ipynb](ground_truth_data/crop_and_zoom_image.ipynb). Our GT data is now ready to use for evaluation (PS scorer and user study)!