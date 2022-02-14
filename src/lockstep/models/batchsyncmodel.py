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
from lockstep.models.companysyncmodel import CompanySyncModel
from lockstep.models.contactsyncmodel import ContactSyncModel
from lockstep.models.creditmemoappliedsyncmodel import CreditMemoAppliedSyncModel
from lockstep.models.invoicesyncmodel import InvoiceSyncModel
from lockstep.models.invoicelinesyncmodel import InvoiceLineSyncModel
from lockstep.models.customfieldsyncmodel import CustomFieldSyncModel
from lockstep.models.paymentsyncmodel import PaymentSyncModel
from lockstep.models.paymentappliedsyncmodel import PaymentAppliedSyncModel

@dataclass
class BatchSyncModel:
    """
    A BatchSyncModel contains a collection of records to load into the
    Lockstep Platform. Data contained in this batch will be merged with
    your existing data. Each record will be matched with existing data
    inside the Lockstep Platform using the [Identity
    Column](https://developer.lockstep.io/docs/identity-columns) rules.
    Any record that represents a new AppEnrollmentId+ErpKey will be
    inserted. A record that matches an existing AppEnrollmentId+ErpKey
    will be updated, but only if the data has changed. A Sync process
    permits either a complete data file or a partial / delta data file.
    Lockstep recommends using a sliding time window to avoid the risk of
    clock skew errors that might accidentally omit records. Best
    practice is to run a Sync process daily, and to export all data that
    has changed in the past 48 hours.
    """

    companies: list[CompanySyncModel] = None
    contacts: list[ContactSyncModel] = None
    creditMemoApplications: list[CreditMemoAppliedSyncModel] = None
    invoices: list[InvoiceSyncModel] = None
    invoiceLines: list[InvoiceLineSyncModel] = None
    customFields: list[CustomFieldSyncModel] = None
    payments: list[PaymentSyncModel] = None
    paymentApplications: list[PaymentAppliedSyncModel] = None

