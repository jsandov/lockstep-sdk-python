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


from dataclasses import dataclass
from lockstep.models.financialreportrowmodel import FinancialReportRowModel

@dataclass
class FinancialReportModel:
    """
    Represents a Financial Report
    """

    reportName: str | None = None
    groupKey: str | None = None
    reportStartDate: str | None = None
    reportEndDate: str | None = None
    reportCreatedDate: str | None = None
    rows: list[FinancialReportRowModel] | None = None

