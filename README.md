# WaterPath Data Schemas

## Data Schemas

This repository includes the data schemas used by the WaterPath project and the [GloWPa model](https://git.wur.nl/glowpa/glowpa-r). The data schemas are defined using the [Tableschema specification](https://specs.frictionlessdata.io/table-schema/) in JSON format. 

The following data types are currently supported:
* Population (*population_schema.json*)
* Sanitation (*sanitation_schema.json*)
* Waste Management (*waste_management_schema.json*)
* Treatment (*treatment_high_resolution_schema.json* **OR** *treatment_schema.json*)

## Data validation scripts

The **example** folder includes an (example) data validation script using a schema file with real data from Kampala, Uganda. The source dataset and individual data files are expressed in CSV format, using a specific decimal system ("." as decimal separator, "," as thousands separator). 

The data validation script runs on Python and the [tableschema](https://pypi.org/project/tableschema/) utility library.