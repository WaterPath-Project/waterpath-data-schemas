from tableschema import Table

errors = []
def exc_handler(exc, row_number=None, row_data=None, error_data=None):
    errors.append((exc, row_number, row_data, error_data))
    print("Error at row #",row_number, ": ", exc)


table = Table('glowpa_isodata_kla_population.csv', schema='../population_schema.json')

for row in table.iter(exc_handler=exc_handler):
    print(".")
    
if errors:
    print('Validation finished unsuccessfully. ', len(errors), ' errors detected!')
else:
    print('Validation finished successfully. No errors detected!')