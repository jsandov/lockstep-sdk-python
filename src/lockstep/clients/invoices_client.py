#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.atriskinvoicesummarymodel import AtRiskInvoiceSummaryModel
from lockstep.models.bulkdeleterequestmodel import BulkDeleteRequestModel
from lockstep.models.deleteresult import DeleteResult
from lockstep.models.invoicemodel import InvoiceModel
from lockstep.models.invoicesummarymodelinvoicesummarytotalsmodelsummaryfetchresult import InvoiceSummaryModelInvoiceSummaryTotalsModelSummaryFetchResult
from requests.models import Response

class InvoicesClient:
    """
    API methods related to Invoices
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_invoice(self, id: str, include: str) -> LockstepResponse[InvoiceModel]:
        """
        Retrieves the Invoice specified by this unique identifier,
        optionally including nested data sets.

        An Invoice represents a bill sent from one company to another.
        The creator of the invoice is identified by the `CompanyId`
        field, and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this invoice; NOT
            the customer's ERP key
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Addresses,
            Lines, Payments, Notes, Attachments, Company, Customer,
            CustomFields, CreditMemos
        """
        path = f"/api/v1/Invoices/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def update_invoice(self, id: str, body: object) -> LockstepResponse[InvoiceModel]:
        """
        Updates an existing Invoice with the information supplied to
        this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        An Invoice represents a bill sent from one company to another.
        The creator of the invoice is identified by the `CompanyId`
        field, and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the invoice to
            update; NOT the customer's ERP key
        body : object
            A list of changes to apply to this Invoice
        """
        path = f"/api/v1/Invoices/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def delete_invoice(self, id: str) -> LockstepResponse[DeleteResult]:
        """
        Deletes the Invoice referred to by this unique identifier. An
        Invoice represents a bill sent from one company to another. The
        creator of the invoice is identified by the `CompanyId` field,
        and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the invoice to
            delete; NOT the customer's ERP key
        """
        path = f"/api/v1/Invoices/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def create_invoices(self, body: list[InvoiceModel]) -> LockstepResponse[list[InvoiceModel]]:
        """
        Creates one or more Invoices within this account and returns the
        records as created.

        An Invoice represents a bill sent from one company to another.
        The creator of the invoice is identified by the `CompanyId`
        field, and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        body : list[InvoiceModel]
            The Invoices to create
        """
        path = "/api/v1/Invoices"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, list[InvoiceModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def delete_invoices(self, body: BulkDeleteRequestModel) -> LockstepResponse[DeleteResult]:
        """
        Delete the Invoices referred to by these unique identifiers.

        An Invoice represents a bill sent from one company to another.
        The creator of the invoice is identified by the `CompanyId`
        field, and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        body : BulkDeleteRequestModel
            The unique Lockstep Platform ID numbers of the Invoices to
            delete; NOT the customer's ERP keys
        """
        path = "/api/v1/Invoices"
        result = self.client.send_request("DELETE", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def query_invoices(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[InvoiceModel]]:
        """
        Queries Invoices for this account using the specified filtering,
        sorting, nested fetch, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        An Invoice represents a bill sent from one company to another.
        The creator of the invoice is identified by the `CompanyId`
        field, and the recipient of the invoice is identified by the
        `CustomerId` field. Most invoices are uniquely identified both
        by a Lockstep Platform ID number and a customer ERP "key" that
        was generated by the system that originated the invoice.
        Invoices have a total amount and a due date, and when some
        payments have been made on the Invoice the `TotalAmount` and the
        `OutstandingBalanceAmount` may be different.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Addresses,
            Lines, Payments, Notes, Attachments, Company, Customer,
            CustomFields, CreditMemos
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Invoices/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult[InvoiceModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def retrieve_invoice_pdf(self, id: str) -> Response:
        """
        Retrieves a PDF file for this invoice if it is of one of the
        supported invoice types and has been synced using an app
        enrollment to one of the supported apps.

        Sage Intacct supports AR Invoices.

        Quickbooks Online supports AR Invoices, and AR Credit Memos.

        Xero supports AR Invoices, AP Invoices, AR Credit Memos, and AP
        Credit Memos.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this invoice; NOT
            the customer's ERP key
        """
        path = f"/api/v1/Invoices/{id}/pdf"
        result = self.client.send_request("GET", path, None, {}, None)
        return result

    def query_invoice_summary_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[InvoiceSummaryModelInvoiceSummaryTotalsModelSummaryFetchResult]:
        """
        Queries Invoices for this account using the specified filtering,
        sorting, nested fetch, and pagination rules requested. Display
        the results using the Invoice Summary View format.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        The Invoice Summary View represents a slightly different view of
        the data and includes some extra fields that might be useful.
        For more information, see the data format of the Invoice Summary
        Model.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Summary, Aging
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Invoices/views/summary"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, InvoiceSummaryModelInvoiceSummaryTotalsModelSummaryFetchResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def query_at_risk_view(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[AtRiskInvoiceSummaryModel]]:
        """
        Queries At Risk Invoices for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested. Display the results using the At Risk Invoice Summary
        View format.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        The At Risk Invoice Summary View represents a slightly different
        view of the data and includes some extra fields that might be
        useful. For more information, see the data format of the At Risk
        Invoice Summary Model.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Invoices/views/at-risk-summary"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult[AtRiskInvoiceSummaryModel](**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
