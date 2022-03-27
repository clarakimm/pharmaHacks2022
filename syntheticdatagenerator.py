import csv
import random

Details = ["Hemoglobin", "Calcium",	"B-2 Microglobulin", "Albumin",	"A Globulin",
           "B Globulin",	"G Globulin", "Osteolytic Lesions",	"Lactate Dehydrogenase", "Type"]

with open ('synthetichealthydata.csv', 'w', newline="" ) as f:
    write = csv.writer(f)
    write.writerow(Details)
    i = 0
    #loop that creates sythetic data points that simuate healthy patients
    while( i < 139 ):
        #defining values
        hgb = round( random.uniform(11.6,16.6), 2 )
        ca = round( random.uniform(86.0,103.0), 2 )
        b2m = round( random.uniform(0.7,1.8), 2 )
        albu = round( random.uniform(34.0,49.3), 2 )
        aGlobu = round( random.uniform(1.0,3.0), 2)
        bGlobu = round( random.uniform(7.0,12.0), 2)
        gGlobu = round( random.uniform(7.0,16.0), 2)
        osteo = 0
        ldh = round( random.uniform(140.0,280.0), 2)
        type = 0

        rows = [[hgb,ca,b2m,albu,aGlobu,bGlobu,gGlobu,osteo,ldh,type]]
        write.writerows(rows)
        i = i + 1

with open ('synthetictestmmdata.csv', 'w', newline="" ) as g:
    write = csv.writer(g)
    write.writerow(Details)

    # loop that creates synthetic data points that simulate multiple myeloma stage one
    j = 0
    while (j < 117):
        # og value 117
        # defining values
        hgb = round(random.uniform(8.42, 12.75), 2)
        ca = round(random.uniform(42.16, 134.36) ,2)
        b2m = round(random.uniform(1.36, 12.51), 2)
        albu = round(random.uniform(28.96, 41.21), 2)
        aGlobu = round(random.uniform(8.07, 14.71), 2)
        bGlobu = round(random.uniform(2.7, 33.87), 2)
        gGlobu = round(random.uniform(3.29, 54.37), 2)
        osteo = round(random.uniform(0, 1))
        ldh = round(random.uniform(130.4, 335.68), 2)
        type = 1

        rows = [[hgb, ca, b2m, albu, aGlobu, bGlobu, gGlobu, osteo, ldh, type]]
        write.writerows(rows)
        j = j + 1

    # loop that creates synthetic data points that simulate multiple myeloma stage two
    k = 0
    while (k < 119):
        # og value 119
        # defining values
        hgb = round(random.uniform(8.18, 13.37), 2)
        ca = round(random.uniform(66.10, 111.01), 2)
        b2m = round(random.uniform(3.19, 5.34), 2)
        albu = round(random.uniform(28.02, 43.45), 2)
        aGlobu = round(random.uniform(8.74, 15.62), 2)
        bGlobu = round(random.uniform(2.7, 33.28), 2)
        gGlobu = round(random.uniform(4.09, 37.01), 2)
        osteo = round(random.uniform(0, 1))
        ldh = round(random.uniform(68, 560.23), 2)
        type = 2

        rows = [[hgb, ca, b2m, albu, aGlobu, bGlobu, gGlobu, osteo, ldh, type]]
        write.writerows(rows)
        k = k + 1

    # loop that creates synthetic data points that simulate multiple myeloma stage three
    l = 0
    while (l < 100):
        # og value 119
        # defining values
        hgb = round(random.uniform(7.52, 12.49), 2)
        ca = round(random.uniform(67.75, 128.07), 2)
        b2m = round(random.uniform(3.10, 8.66), 2)
        albu = round(random.uniform(25.66, 39.72), 2)
        aGlobu = round(random.uniform(7.31, 15.95), 2)
        bGlobu = round(random.uniform(2.7, 34.09), 2)
        gGlobu = round(random.uniform(1.37, 53.95), 2)
        osteo = 1
        ldh = round( random.uniform(211.41,670.28), 2)
        type = 3

        rows = [[hgb, ca, b2m, albu, aGlobu, bGlobu, gGlobu, osteo, ldh, type]]
        write.writerows(rows)
        l = l + 1

