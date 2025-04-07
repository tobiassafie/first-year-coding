# Philadelphia Displacement Tool

A visual analysis of displacement patterns in modern-day Philadelphia, exploring the long-term impacts of redlining through rent inflation, household income changes, and demographic shifts across census tracts.

## Overview

This tool visualizes:
- 1930s HOLC redlining zones
- Median rent changes (2010–2020)
- Demographic shifts (race, income) per tract

The goal is to understand how historical housing discrimination still correlates with present-day displacement pressures.

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
- `README_displacement.md`: This file — specific to the Displacement Tool

## Design Process & Challenges

This tool began as a way to explore how historical redlining relates to modern displacement. Designing it required careful thinking about how to combine historical and contemporary datasets with different spatial boundaries and formats.

### Key challenges:
- **Spatial crosswalks:** Aligning 1930s HOLC zones with modern census tracts was non-trivial due to boundary shifts and inconsistencies. I used a pre-built GeoJSON crosswalk but still had to check for mismatches.
- **Data cleaning + matching:** Matching different datasets via their unique GEOIDS, GEOJSONS, and tract ids. However, ACS and Eviction Lab datasets had different formats, time spans, and missing values. Because of this and my current schedule + skill level, I opted to omit the eviction data for the time being, until I'm more comfortable with this kind of data analysis. 
- **Balancing clarity and depth:** Choosing how much to show on the map (e.g., rent, race, eviction) without overwhelming the user required thoughtful UI decisions.

### Design choices:
- Built around census tracts for precision and consistency with demographic/economic data
- Prioritized interactive storytelling over pure data dumping — map layers guide users through a narrative
- Focused on rent, income, and racial demographic as key metrics for displacement, due to their immediacy and emotional relevance

## Author & Purpose

Created by Tobias Safie as part of a broader effort to analyze gentrification and housing inequality in Philadelphia. This project serves as both a data science exercise, an extension to a prior research project, and, most importantly, a contribution to ongoing urban justice conversations. Specifically for me, I want to bridge the gap between data science and social justice to actually help people.
