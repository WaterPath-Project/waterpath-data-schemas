from tableschema import Table
from pprint import pprint
from frictionless import describe, validate, checks, Resource, Package, Checklist

errors = []
def exc_handler(exc, row_number=None, row_data=None, error_data=None):
    errors.append((exc, row_number, row_data, error_data))
    print("Error at row #",row_number, ": ", exc)
    
package = Package('datapackage.json')

checklist = Checklist()

for resource in package.resources:
  if resource.name == 'sanitation':
    report = validate(resource, checks=[checks.row_constraint(formula='flushSewer_rur + flushSeptic_rur + flushPit_rur + flushOpen_rur + flushUnknown_rur + pitSlab_rur + pitNoSlab_rur + compostingToilet_rur + bucketLatrine_rur + containerBased_rur + hangingToilet_rur + openDefecation_rur + other_rur == 1'),checks.row_constraint(formula='flushSewer_urb + flushSeptic_urb + flushPit_urb + flushOpen_urb + flushUnknown_urb + pitSlab_urb + pitNoSlab_urb + compostingToilet_urb + bucketLatrine_urb + containerBased_urb + hangingToilet_urb + openDefecation_urb + other_urb == 1')])
  elif resource.name == 'waste_management':
    report = validate(resource)
  else:
    report = validate(resource)
  pprint(report.flatten(["type", "message"]))
