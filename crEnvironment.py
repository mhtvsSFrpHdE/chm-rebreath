# 3rd

# Environment
import pathlib  # Path

# Log
import logging

# My
import crDevInput  # Information used while development
import crMagicValue
import crMessage

from crLog import crPrintCyan

# Scan and get catalog file path


def get_catalog_file_path():
    catalogFilePath = None

    try:
        catalogFileList = pathlib.Path(crDevInput.unpackedChmFolder).glob(
            crMagicValue.chmCatalogFileSearchPattern)
        catalogFileListCount = 0

        for catalogFile in catalogFileList:
            catalogFileListCount = catalogFileListCount + 1

            if catalogFileListCount > 1:
                crPrintCyan(crMessage.errMultipleCatalogFile)
                raise EnvironmentError(crMessage.errMultipleCatalogFile)

            catalogFilePath = catalogFile

        if catalogFileListCount is 0:
            crPrintCyan(crMessage.errCatalogFileNotFound)
            raise EnvironmentError(crMessage.errCatalogFileNotFound)
    except:
        logging.exception(__name__)
        raise

    return catalogFilePath
