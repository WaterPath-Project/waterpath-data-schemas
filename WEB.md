# WaterPath Toolkit Data Schemas

At the core of the WaterPath Toolkit, data schemas are used to formally define the structure, types, and constraints of the input and output data involved in the developed tools. A data schema serves as a blueprint that ensures consistency, validation, and interoperability across components by specifying how data should be organized and interpreted. Data conforming to these schemas can be reliably parsed and consumed by the [GloWPa model](https://git.wur.nl/glowpa/glowpa-r), resulting in robust results and minimized errors and inconsistencies. 

All data schemas in the WaterPath Toolkit are defined using the [Tableschema specification](https://specs.frictionlessdata.io/table-schema/) and expressed in JSON format. They are openly available on our [Github repository](https://github.com/WaterPath-Project/waterpath-data-schemas).

The following data types are currently supported:
* Population (*population_schema.json*)
* Sanitation (*sanitation_schema.json*)
* Treatment (*treatment_high_resolution_schema.json* **OR** *treatment_schema.json*)
