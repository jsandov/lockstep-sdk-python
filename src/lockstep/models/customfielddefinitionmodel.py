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
class CustomFieldDefinitionModel:
    """
    A Custom Field represents metadata added to an object within the
    Lockstep Platform. Lockstep provides a core definition for each
    object. The core definition is intended to represent a level of
    compatibility that provides support across most accounting systems
    and products. When a user or developer requires information beyond
    this core definition, you can use Custom Fields to represent this
    information. See [Extensibility](https://developer.lockstep.io/docs/extensibility)
    for more information.
    """

    groupKey: str | None = None
    customFieldDefinitionId: str | None = None
    tableKey: str | None = None
    appId: str | None = None
    customFieldLabel: str | None = None
    dataType: str | None = None
    sortOrder: int | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None

