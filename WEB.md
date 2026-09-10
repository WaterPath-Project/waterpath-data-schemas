# WaterPath Toolkit Data Schemas

At the core of the WaterPath Toolkit, data schemas are used to formally define the structure, types, and constraints of the input and output data involved in the developed tools. A data schema serves as a blueprint that ensures consistency, validation, and interoperability across components by specifying how data should be organized and interpreted. Data conforming to these schemas can be reliably parsed and consumed by the [GloWPa model](https://git.wur.nl/glowpa/glowpa-r), resulting in robust results and minimized errors and inconsistencies. 

All data schemas in the WaterPath Toolkit are defined using the [Tableschema specification](https://specs.frictionlessdata.io/table-schema/) and expressed in JSON format. They are openly available on our [Github repository](https://github.com/WaterPath-Project/waterpath-data-schemas).

The following data types are currently supported:
* Human Population (*human_emissions_isodata.json*)
* Sanitation (*human_emissions_sanitation.json*)
* Treatment (*human_emissions_point_treatment.json* **OR** *human_emissions_treatment.json*)
* Livestock population (*livestock_isodata.json*)
* Livestock manure fractions (*livestock_manure_fractions.json*)
* Livestock manure management (*livestock_manure_management.json*)
* Livestock production systems (*livestock_production_systems.json*)
