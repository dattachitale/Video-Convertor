"""
Module to fetch csv data and bulk index it into Elasticsearch Server

Created by Saurabh Rukmangad and Pooja Sahu, QC Automation Pune for Project Vortex
"""
import sys
import os
import csv
import socket
import logging
from datetime import date
from configparser import ConfigParser
from elasticsearch import helpers, Elasticsearch
import logging.config

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})


def insert_file_Elasticsearch(filepath, indexname):
    """
    Function to insert csv file data into elasticsearh index

    Args:
        filepath: string
        indexname: string

    Return:
        True/False: boolean
    """
    # Set the logging level and logging format
    FORMAT = '[Elasticsearch] %(asctime)s %(funcName)s %(lineno)d %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, filename='elasticsearch_python.log')

    # Read host IP and Port from elasticsearchConfig.ini file
    configfile = "elasticsearch_config.ini"

    # Credentials
    elasticUser = 'elastic'
    elasticPSWD = 'Ed1rZR1sN1caXPSAe--R'

    # If the file exists
    if os.path.isfile(configfile):
        config = ConfigParser()
        config.read(configfile)

        # fetch host name and port number
        hostIP = config["host-details"]["IP"]
        print(f'HOST-IP: {hostIP}')
        portnumber = config["host-details"]["Port"]
        print(f'PORT: {portnumber}')
        logging.info("Config file details - host: %s", hostIP)
        logging.info("Config file details - portnumber: %s", portnumber)

    else:
        # if file doesn't exist
        hostIP = "localhost"
        portnumber = "9200"

        logging.info("Config file does not exist - default host: %s", hostIP)
        logging.info("Config file does not exist - default portnumber: %s", portnumber)

    # Create elasticsearch instance
    es = Elasticsearch([{'host': hostIP, 'port': portnumber}], http_auth=(elasticUser, elasticPSWD),
                       verify_certs=True)
    print(f'ES: {es}')

    # Ping the Elasticsearh server to know if it is up
    if not es.ping():
        logging.info("Cannot connect to Elasticsearch Engine")
        return False

    # If ping response not False, means elasticsearch is up
    print("[Elasticsearch]: Connection Established with Elasticsearch Engine: ", hostIP)
    logging.info("Connection Established with Elasticsearch Engine: %s", str(hostIP))

    # Create pipeline setting
    timestamp_host_pipeline_setting = {
        "description": "insert timestamp and host field for all documents", "processors":
            [
                {
                    "set": {
                        "field": "timestamp",
                        "value": "{{_ingest.timestamp}}"
                    }
                },
                {
                    "set": {
                        "field": "host",
                        "value": socket.gethostname()
                    }
                }
            ]
    }

    # ingest pipeline setting
    es.ingest.put_pipeline("timestamp_host_pipeline", timestamp_host_pipeline_setting)

    # Prepare configuration
    conf = {
        "settings":
            {
                "default_pipeline": "timestamp_host_pipeline"
            },
        "mappings":
            {
                "numeric_detection": True
            }
    }

    # Create index with config settings if it does not exist already
    # ignore 400 already exists code
    response = es.indices.create(index=indexname, body=conf, ignore=400)
    logging.info("Index create response: %s", str(response))

    # Check if the index exists
    if es.indices.exists(index=indexname):
        # open the file and bulk insert the contents in index
        with open(filepath) as file:
            print(f'FILEPATH: {filepath}')
            try:
                reader = csv.DictReader(file)
                print(f'indexname: {indexname}')

                resp = helpers.bulk(es, reader, index=indexname)
                print(f'RESPONSE: {resp}')
                print("[Elasticsearch]: Number of Records inserted: ", resp[0])
                logging.info("Number of Records inserted: %s", str(resp[0]))
            except Exception as e:
                print("Unexpected error:")
                print(e)
                logging.info("[ERROR] Unexpected error: %s", str(e))
                # Explicitly close the connection
                es.close()
                return False

        # Explicitly close the connection
        es.close()
        print("[Elasticsearch]: Inserted data into index: ", indexname)
        logging.info("Inserted data into index: %s", indexname)

    else:
        print("[Elasticsearch]: Index Does Not Exist: ", indexname)
        logging.warning("[Elasticsearch]: Index Does Not Exist: ", indexname)

    logging.info("--------------------------------------------------------------------------------------------------")
    return True
