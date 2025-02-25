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

@dataclass
class CodeDefinitionModel:
    """
    Represents a Code Definition. Codes can be used as shortened, human
    readable strings. Additionally, this table can be used to store
    lists of system values for Lockstep objects.
    """

    codeDefinitionId: str | None = None
    groupKey: str | None = None
    codeType: str | None = None
    code: str | None = None
    codeDescription: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

