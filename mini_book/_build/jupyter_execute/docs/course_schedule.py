## Course schedule

Here is the current week-by-week schedule 📅 . We may adjust as we go along. To get started, we're going to create the calendar of weeks for the course programmatically rather than manually!


## import modules
import pandas as pd
import re
import numpy as np


## tell python to display output and print multiple objects
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## create range b/t start and end date
## of course 
start_date = pd.to_datetime("2021-03-29")
end_date = pd.to_datetime("2021-06-02")
st_alldates = pd.date_range(start_date, end_date)

## subset to days in that range equal to Tuesday or Thursday
st_tuth = st_alldates[st_alldates.day_name().isin(['Tuesday', 'Thursday'])]

## create data frame with that information
st_dates = [re.sub("2021\\-", "", str(day.date())) for day in st_tuth] 
course_sched = pd.DataFrame({'dow': st_tuth.day_name(), 'st_tuth': st_dates})
course_sched['date_toprint'] = course_sched.dow.astype(str) + " " + \
            course_sched.st_tuth.astype(str) 
course_sched = course_sched['date_toprint']

## display the resulting date sequence
display(course_sched)

## next block of code creates the
## actual content; can click "show"
## to see the underlying code

## create the actual content

### list of concepts
concepts = ["Course intro. and checking software setup",
             "Workflow basics: command line, Github workflow, basic LaTeX syntax, pre-analysis plans",
             "Python basic data wrangling: data structures (vectors; lists; dataframes; matrices), control flow, and loops",
             "Python basic data wrangling: basic regular expressions and text mining",
             "Python basic data wrangling: combining data (row binds, column binds, joins); aggregation",
             "Review of visualization: ggplot; plotnine",
            "Problem set one review",
             "Python: writing your own functions and simulation",
             "Python: text data using nltk and gensim",
             "Python: spatial data using geopandas",
             "SQL: reading data from a database and basic SQL (postgres) syntax",
             "SQL: more advanced SQL syntax (subqueries; window functions)",
             "Python: reading data from APIs and basic web scraping",
             "Python: interacting with cloud computing resources (Amazon S3; Dartmouth's Andes or Polaris servers)",
            "Problem set two review",
             "Interactive visualization: bokeh in Python",
             "Workflow: Beamer",
             "Workflow: Beamer and Tikz graphics",
             "Final presentations"]

## combine
course_sched_concepts = pd.DataFrame({'Week': course_sched,
                                     'Concepts': concepts})

df = course_sched_concepts.copy()

## add datacamp modules conditionally
col = "Concepts"
topics  = [df[col] == "Python basic data wrangling: data structures (vectors; lists; dataframes; matrices), control flow, and loops", 
               df[col] == "Python basic data wrangling: basic regular expressions and text mining",
               df[col] ==  "Python basic data wrangling: combining data (row binds, column binds, joins); aggregation",
               df[col] == "Review of visualization: ggplot; plotnine",
               df[col] == "Python: writing your own functions",
               df[col] == "Python: text data using nltk and gensim",
               df[col] ==  "SQL: reading data from a database and basic SQL (postgres) syntax",
               df[col] == "SQL: more advanced SQL syntax (subqueries; window functions)",
               df[col] == "Python: reading data from APIs and basic web scraping"]
datacamp_modules = ["Python basics; python lists; Pandas: extracting and transforming data; Intermediate python for data science (loops)",
                   "First three modules of regular expressions in Python",
                   "Merging DataFrames with Pandas",
                   "Introduction to Data Visualization with ggplot2",
                   "Python data science toolbox (Part one): user-written functions, default args, lambda functions and error handling",
                   "Natural language processing fundamentals in Python",
                   "Introduction to databases in Python",
                   "Intermediate SQL",
                   "Importing JSON data and working with APIs; Importing data from the Internet"]

df["DataCamp module(s) (if any)"] = np.select(topics, 
                                     datacamp_modules, 
                                     default = "")


date_col = "Week"
due_dates = [df[date_col] == "Thursday 04-15",
            df[date_col] == "Thursday 04-22",
            df[date_col] == "Thursday 05-13",
            df[date_col] == "Tuesday 06-01"]
assig = ["Problem set one",
        "1-page project proposal",
        "Problem set two",
        "Slides for final presentation (due Monday 05.31 at 9 am)"]

df["Due (11:59 PM EST unless otherwise specified)"] = np.select(due_dates,
                     assig,
                     default = "")


HTML(df.to_html(index=False))