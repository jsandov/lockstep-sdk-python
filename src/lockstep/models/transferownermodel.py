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
from lockstep.models.useraccountmodel import UserAccountModel
from lockstep.models.useraccountmodel import UserAccountModel

@dataclass
class TransferOwnerModel:
    """
    Model from the transfer ownership process.
    """

    previousOwner: UserAccountModel | None = None
    newOwner: UserAccountModel | None = None

