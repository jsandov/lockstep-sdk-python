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

@dataclass
class CreditMemoInvoiceModel:
    """
    Contains information about a credit memo invoice
    """

    groupKey: str | None = None
    creditMemoAppliedId: str | None = None
    invoiceId: str | None = None
    creditMemoInvoiceId: str | None = None
    applyToInvoiceDate: str | None = None
    creditMemoAppliedAmount: float | None = None
    referenceCode: str | None = None
    companyId: str | None = None
    customerId: str | None = None
    invoiceStatusCode: str | None = None
    totalAmount: float | None = None
    outstandingBalanceAmount: float | None = None

