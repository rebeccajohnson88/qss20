---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(course_schedule)=


## Course schedule

Here is the current week-by-week schedule. We may adjust as we go along. To get you started, we're going to create the calendar of weeks for the course programmatically rather than manually!


```{code-cell} python3
## import modules
import pandas as pd
import re

## display output
from IPython.display import display, HTML

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

## display the result
display(course_sched)
```
