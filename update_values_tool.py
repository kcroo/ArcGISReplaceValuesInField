# Author: Kirsten Corrao
# Date: 1/16/2020
# Description: this tool takes 4 parameters for a shapefile, the field to update, the data to replace in that field, and what to replace it with.

import arcpy 

try: 
    arcpy.env.overwriteOutput = True

    file_param = arcpy.GetParameterAsText(0)
    field_param = arcpy.GetParameterAsText(1)
    search_param = arcpy.GetParameterAsText(2)
    replace_param = arcpy.GetParameterAsText(3)

except Exception as error:
    print("Problem while making parameters and workspace", error)

# for each in shapefile (update): 
try:
    where_clause = """"{}" = '{}'""".format(field_param, search_param)

    with arcpy.da.UpdateCursor(file_param, field_param, where_clause) as cursor:
        for row in cursor:
            row[0] = replace_param
            cursor.updateRow(row)

    del cursor

except Exception as error:
    print("Problem updating fields", error)
