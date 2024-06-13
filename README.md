# Folder Structure

### Components:

##### Excel Data [FOLDER]:
- - Local download of the excel files for the challenge
- Is touched by:
- - Request and Quote Migration (single use notebook)
  - Used to migrate the data to a MongoDB
  - Imports can now be handled by <opply_resources.py> makeshift module

##### Data Cleaning and ETL and EDA (Bronze to Silver) [NOTEBOOK]:
- - Contains etl and eda processes that created the data used for later analysis
  - Is also a single-use notebook for the purpose of this task, though will not impact other work if re-run.

##### Silver Data [FOLDER]:
- - contains data from EDA/ETL step

##### Conversion Data Analysis [NOTEBOOK]:
- - Contains work that answers questions of the data relative to conversion ratio
  - Also contains markdown write-ups as to the findings of the data.

##### Write Up [FOLDER]:
- - contains single document for points 4 and 5 of the brief.
