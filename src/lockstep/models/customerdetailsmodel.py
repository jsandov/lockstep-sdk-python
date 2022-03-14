#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.customerdetailspaymentmodel import CustomerDetailsPaymentModel

@dataclass
class CustomerDetailsModel:
    """
    Contains customer details data
    """

    groupKey: str | None = None
    customerId: str | None = None
    name: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    state: str | None = None
    postalCode: str | None = None
    country: str | None = None
    phoneNumber: str | None = None
    faxNumber: str | None = None
    email: str | None = None
    contactId: str | None = None
    contactName: str | None = None
    contactEmail: str | None = None
    outstandingInvoices: int | None = None
    outstandingAmount: float | None = None
    amountPastDue: float | None = None
    payments: list[CustomerDetailsPaymentModel] | None = None

