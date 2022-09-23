#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:56:54 2022

@author: john.omole
"""


import logging
import os
import requests

logging.basicConfig(format="%(asctime)s %(name)s %(levelname)-10s %(message)s")
LOG = logging.getLogger("API")
LOG.setLevel(os.environ.get("LOG_LEVEL", logging.DEBUG))

##############################################################################
LOG.info("init parameters")
#############################################################################

class API():
    def __init__(self):
        """

        Returns
        -------
        None.

        """
        self.base_url = "https://619ca0ea68ebaa001753c9b0.mockapi.io/evaluation/dataengineer/jr/v1/"

    def __str__(self):
        pass

    def _get_api_information(self, endpoint):
        """

        Parameters
        ----------
        endpoint : TYPE
            DESCRIPTION.

        Returns
        -------
        resp : TYPE
            DESCRIPTION.

        """
        url = f"{self.base_url}{endpoint}"
        
        payload={
          
        }
        headers = {
        }
        
        response = requests.request("GET", url, headers=headers, data=payload)
    
        resp = response.json()

        return resp



