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

from src.lockstep.models.financialreportrowmodel import FinancialReportRowModel


@dataclass
class FinancialReportModel:
    """
    Represents a Financial Report
    """

    reportName: str = None
    groupKey: str = None
    reportStartDate: str = None
    reportEndDate: str = None
    reportCreatedDate: str = None
    rows: list[FinancialReportRowModel] = None

