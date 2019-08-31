def saveDataToCSV(dictList, fileLocation):
    import csv
    keys = dictList[0].keys()
    with open(fileLocation, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictList)