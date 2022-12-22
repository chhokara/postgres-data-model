# Project Purpose
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The data engineer's role is to create a database schema and ETL pipeline for this analysis. They will be able to test their database and ETL pipeline by running queries given to them by the analytics team from Sparkify and compare their results with the expected results.

*Source: Udacity Project Introduction

# Running Python Scripts
There are two main scripts that need to be run in this project. The first is "create_tables.py" which can be run with the command "python create_table.py". The second is "etl.py" which can be run with the command "python etl.py".

# Project Files
## data
This folder contains the respective directories for log data and song data.

## create_tables.py
Contains python functions that create the sparkify database and run queries for creating and dropping tables.

## etl.ipynb
Notebook containing instructions on how to develop ETL processes for each table.

## etl.py
Contains python functions which implement an ETL pipeline in order to process the entire datasets.

## sql_queries.py
Contains SQL queries for dropping tables, creating tables, inserting records, and selecting data.

## test.ipynb
Notebook that is used to confirm that records were inserted correctly into each table. This notebook also contains sanity tests to catch any silly mistakes.

# Project Design
## Database Schema
The STAR schema was used to model the database. This schema contains one fact table called the "song_plays" table, and four dimension tables: "users", "songs", "artists", and "time". This schema is benefitial because the tables are denormalized which makes queries simpler and aggregations faster.

## ETL Pipeline
The ETL pipeline extracts data from the song and log files, transforms the data into the correct format using appropriate data structures, and finally loads that data into the PostgreSQL tables.