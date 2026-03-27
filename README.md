# WaterPath Data Schemas

## Data Schemas

This repository includes the data schemas used by the WaterPath project and the [GloWPa model](https://git.wur.nl/glowpa/glowpa-r). The data schemas are defined using the [Tableschema specification](https://specs.frictionlessdata.io/table-schema/) in JSON format and correspond to the main drivers that affect microbial pollution, both in surface water and land. 

The following data types are currently supported:
* Human Population (*human_emissions_isodata.json*)
* Sanitation (*human_emissions_sanitation.json*)
* Treatment (*human_emissions_point_treatment.json* **OR** *human_emissions_treatment.json*)
* Livestock population (*livestock_isodata.json*)
* Livestock manure fractions (*livestock_manure_fractions.json*)
* Livestock manure management (*livestock_manure_management.json*)
* Livestock production systems (*livestock_production_systems.json*)

## Data validation scripts

The **example** folder includes an (example) data validation script for a human emissions scenario using a schema file with real data from Kampala, Uganda. The source dataset and individual data files are expressed in CSV format, using a specific decimal system ("." as decimal separator, "," as thousands separator). 

The data validation script runs on Python and the [tableschema](https://pypi.org/project/tableschema/) utility library.
