# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ValidateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_reference_information': 'Riskv1decisionsClientReferenceInformation',
        'processing_information': 'Riskv1authenticationsetupsProcessingInformation',
        'order_information': 'Riskv1authenticationresultsOrderInformation',
        'payment_information': 'Riskv1authenticationresultsPaymentInformation',
        'consumer_authentication_information': 'Riskv1authenticationresultsConsumerAuthenticationInformation'
    }

    attribute_map = {
        'client_reference_information': 'clientReferenceInformation',
        'processing_information': 'processingInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation'
    }

    def __init__(self, client_reference_information=None, processing_information=None, order_information=None, payment_information=None, consumer_authentication_information=None):
        """
        ValidateRequest - a model defined in Swagger
        """

        self._client_reference_information = None
        self._processing_information = None
        self._order_information = None
        self._payment_information = None
        self._consumer_authentication_information = None

        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if processing_information is not None:
          self.processing_information = processing_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this ValidateRequest.

        :return: The client_reference_information of this ValidateRequest.
        :rtype: Riskv1decisionsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this ValidateRequest.

        :param client_reference_information: The client_reference_information of this ValidateRequest.
        :type: Riskv1decisionsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this ValidateRequest.

        :return: The processing_information of this ValidateRequest.
        :rtype: Riskv1authenticationsetupsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this ValidateRequest.

        :param processing_information: The processing_information of this ValidateRequest.
        :type: Riskv1authenticationsetupsProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def order_information(self):
        """
        Gets the order_information of this ValidateRequest.

        :return: The order_information of this ValidateRequest.
        :rtype: Riskv1authenticationresultsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this ValidateRequest.

        :param order_information: The order_information of this ValidateRequest.
        :type: Riskv1authenticationresultsOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this ValidateRequest.

        :return: The payment_information of this ValidateRequest.
        :rtype: Riskv1authenticationresultsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this ValidateRequest.

        :param payment_information: The payment_information of this ValidateRequest.
        :type: Riskv1authenticationresultsPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this ValidateRequest.

        :return: The consumer_authentication_information of this ValidateRequest.
        :rtype: Riskv1authenticationresultsConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this ValidateRequest.

        :param consumer_authentication_information: The consumer_authentication_information of this ValidateRequest.
        :type: Riskv1authenticationresultsConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ValidateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
