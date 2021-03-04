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


class Vasv2taxClientReferenceInformation(object):
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
        'code': 'str',
        'partner': 'Riskv1decisionsClientReferenceInformationPartner',
        'comments': 'str'
    }

    attribute_map = {
        'code': 'code',
        'partner': 'partner',
        'comments': 'comments'
    }

    def __init__(self, code=None, partner=None, comments=None):
        """
        Vasv2taxClientReferenceInformation - a model defined in Swagger
        """

        self._code = None
        self._partner = None
        self._comments = None

        if code is not None:
          self.code = code
        if partner is not None:
          self.partner = partner
        if comments is not None:
          self.comments = comments

    @property
    def code(self):
        """
        Gets the code of this Vasv2taxClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization** Required field.  #### PIN Debit Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being reversed.  Required field for all PIN Debit requests (purchase, credit, and reversal).  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :return: The code of this Vasv2taxClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Vasv2taxClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization** Required field.  #### PIN Debit Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being reversed.  Required field for all PIN Debit requests (purchase, credit, and reversal).  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :param code: The code of this Vasv2taxClientReferenceInformation.
        :type: str
        """

        self._code = code

    @property
    def partner(self):
        """
        Gets the partner of this Vasv2taxClientReferenceInformation.

        :return: The partner of this Vasv2taxClientReferenceInformation.
        :rtype: Riskv1decisionsClientReferenceInformationPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this Vasv2taxClientReferenceInformation.

        :param partner: The partner of this Vasv2taxClientReferenceInformation.
        :type: Riskv1decisionsClientReferenceInformationPartner
        """

        self._partner = partner

    @property
    def comments(self):
        """
        Gets the comments of this Vasv2taxClientReferenceInformation.
        Comments

        :return: The comments of this Vasv2taxClientReferenceInformation.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Vasv2taxClientReferenceInformation.
        Comments

        :param comments: The comments of this Vasv2taxClientReferenceInformation.
        :type: str
        """

        self._comments = comments

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
        if not isinstance(other, Vasv2taxClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
