from processDataManager import downloadFile
from processData import processFiles
from getData import getDataHelper, getDataCustomRange
from datetime import datetime, timedelta
from Averaging import AverageTempManager



def main(startDate, endDate, dataPath, processedDataPath):
    filesToProcess = []

    # Get most recent data
    data = getDataCustomRange(printData=False, startDate=startDate, endDate=endDate)
    for entry in data["feed"]["entry"]:
        filename = entry["producer_granule_id"]
        links = entry["links"]
        downloadLink = links[0]["href"]

        # Downlod the file
        downloadFile(downloadLink, "Data/" + filename)
        filesToProcess.append(filename)


    # process new data
    for file in filesToProcess:
        processFiles(file, "ProcessedData/" + file.replace(".h5", ".geojson"))
        AverageTempManager("ProcessedData/" + file.replace(".h5", ".geojson"))


if __name__ == "__main__":
    currentTime = datetime.now()
    startDate = "2022-01-01" # ISO format
    endDate =  "2023-02-01"# ISO format
    dataPath = "Data/"
    processedDataPath = "ProcessedData/"

    main(startDate, endDate, dataPath, processedDataPath)
