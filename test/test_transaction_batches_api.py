# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.transaction_batches_api import TransactionBatchesApi


class TestTransactionBatchesApi(unittest.TestCase):
    """ TransactionBatchesApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.transaction_batches_api.TransactionBatchesApi()

    def tearDown(self):
        pass

    def test_get_transaction_batch_details(self):
        """
        Test case for get_transaction_batch_details

        Get transaction details for a given batch id
        """
        pass

    def test_get_transaction_batch_id(self):
        """
        Test case for get_transaction_batch_id

        Get individual batch file
        """
        pass

    def test_get_transaction_batches(self):
        """
        Test case for get_transaction_batches

        Get a list of batch files
        """
        pass


if __name__ == '__main__':
    unittest.main()
