"""
Generate a SQLite database of all the dataset data from all the courses for an organisation
"""

import os
import sqlite3

from fl_data_downloader import login, get_dataset_for_course, get_courses, DATASETS, DatasetNotFoundForCourse

db_file = "all_courses.db"

if os.path.exists(db_file):
    print("Deleting old database")
    os.remove(db_file)

conn = sqlite3.connect(db_file)

b = login()

# get the courses
courses_df = get_courses(b, raspberry-pi)

# get a list of all the course names
courses = list(courses_df.index.values)

# for each course download all the datasets and append to tables
count = 0
for course in courses: 
    count += 1
    print("{} - {} of {}".format(course, count, len(courses)))

    for dataset in DATASETS:
        print(dataset)
        try:
            df = get_dataset_for_course(b, course=course, dataset=dataset)
            df.to_sql(dataset, conn, if_exists="append")

        except DatasetNotFoundForCourse:
            print("- dataset not found")
        
conn.close()