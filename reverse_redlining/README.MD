# Reverse Redlining - Philadelphia Displacement Mapping Tool

A visual analysis of displacement patterns in modern-day Philadelphia, exploring the long-term impacts of redlining through rent inflation, household income changes, and demographic shifts across census tracts.

## Overview

This tool visualizes:
- 1930s HOLC redlining zones
- Median rent changes (2010–2020)
- Demographic shifts (race, income) per tract

The goal is to understand how historical housing discrimination still correlates with present-day displacement pressures.

## Displacement Map Snapshots

### HOLC Redlining Map of Philadelphia (1930s)
<img src="../assets/Screenshot_whole_map.png" alt="HOLC Redlining Map" width="700"/>

### Tract-level data popup (Northern Liberties)
<img src="../assets/Screenshot_Nolibs.png" alt="Tract popup - Nolibs" width="700"/>

### Tract-level data popup (West Philly)
<img src="../assets/Screenshot_west.png" alt="Tract popup - West Philly" width="700"/>

---

## Data Visualizations from the Displacement Tool

### Rent Change vs Black Population Change in D-Graded (Redlined) Tracts
<img src="../assets/Screenshot_rent_scatterplot.png" alt="Scatterplot rent vs Black pop in D tracts" width="650"/>
In formerly redlined (D-graded) areas, rent rises often coincide with significant drops in Black population, suggesting direct displacement.

### Average Rent Change by HOLC Grade (2010–2020)
<img src="../assets/Screenshot_rent_redlining.png" alt="Bar chart - rent by HOLC grade" width="650"/>
D-graded areas— once starved of investment —now have the largest rent increases, underscoring the direct outcomes of reverse redlining.

### Choropleth: Rent Change by Census Tract
<img src="../assets/rent_change_choropleth.png" alt="Choropleth of rent change" width="650"/>
This choropleth gives a citywide view of how deeply rent increases have affected Philadelphia. The darkest reds mark neighborhoods under the highest displacement pressure. 
  N.B. The darkest red spot is around 38th & Walnut, which is predominantly inhabited by UPenn and Drexel students.


## Data Sources

- [Eviction Lab](https://evictionlab.org/) tract-level data
- [ACS 5-Year Estimates](https://www.census.gov/programs-surveys/acs/) (2010 & 2020)
- HOLC Redlining Map Overlays from [Mapping Inequality](https://dsl.richmond.edu/panorama/redlining/)
- GeoJSON crosswalk to match HOLC zones with modern tracts

## Features

- Interactive map showing income shifts, racial differences, and rent increases by census tract
- Historical redlining overlay toggle
- Demographic change filters

## Technologies Used

- Python (Jupyter Notebook)
- Pandas / GeoPandas
- Folium / Mapbox for mapping
- Conda environment for reproducibility

## Running the Tool

1. Clone this repository
2. Navigate to the `reverse_redlining` folder
3. Launch the Jupyter Notebook
4. Run all cells to load data and generate the map

## Related Files

- `reverse_redlining.ipynb`: Main notebook with full analysis and visualizations
- `\data`: Data folder containing relevant files needed for map projections
- `Redlining_Essay_and_Displacement_Context_TobiasSafie.pdf`: Research paper I wrote on this very topic; inspired this project
- `README_displacement.md`: This file— specific to the Displacement Tool

## Design Process & Challenges

This tool began as a way to explore how historical redlining relates to modern displacement. Designing it required careful thinking about how to combine historical and contemporary datasets with different spatial boundaries and formats.

### Key challenges:
- **Spatial crosswalks:** Aligning 1930s HOLC zones with modern census tracts was non-trivial due to boundary shifts and inconsistencies. I used a pre-built GeoJSON crosswalk but still had to check for mismatches.
- **Data cleaning + matching:** Matching different datasets via their unique GEOIDS, GEOJSONS, and tract ids. However, ACS and Eviction Lab datasets had different formats, time spans, and missing values. Because of this and my current schedule + skill level, I opted to omit the eviction data for the time being, until I'm more comfortable with this kind of data analysis. 
- **Balancing clarity and depth:** Choosing how much to show on the map (e.g., rent, race, eviction) without overwhelming the user required thoughtful UI decisions.

### Design choices:
- Built around census tracts for precision and consistency with demographic/economic data
- Prioritized interactive storytelling over pure data dumping; map layers guide users through a narrative
- Focused on rent, income, and racial demographic as key metrics for displacement, due to their immediacy and relevance

## [The Paper](Redlining_Essay_and_Displacement_Context_TobiasSafie.pdf)
This whole project was inspired by a research paper I wrote for my Fall term English course. We were instructed to write a research paper on any topic of our choice and that it must have a soft 1000 word cutoff so, if selected, could be published in the student research anthology. I of course wrote about displacement in Philadelphia and how historic redlining still affects people to this day. I also didn't meet the word cutoff: I was at about 1300 words after an hour and a half of cutting. This is a vast topic that can be extensively explored— cutting anymore content would be a sin. This is why I planned to create the displacement tool. I wanted to explore this topic of redlining, reverse redlining, gentrification, and displacement further. With this project currently, I want to help spark this conversation in general, but, most importantly, amongst Philadelphia residents to see what we can do to create a more equitable city.

## Author & Purpose

Created by Tobias Safie as part of a broader effort to analyze gentrification and housing inequality in Philadelphia. This project serves as both a data science exercise, an extension to a prior research project, and, most importantly, a contribution to ongoing urban justice conversations. Specifically for me, I want to bridge the gap between data science and social justice to actually help people.
