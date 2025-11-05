from src import dataclean as dc
from src import visualization as viz
from src import correlation as corr


data = dc.load_clean_create_metrics("data/YEAR 4 ASSIGNMENT AND TEST.xlsx")


viz.visualizations(data)


corr.correlation_analysis(data)
