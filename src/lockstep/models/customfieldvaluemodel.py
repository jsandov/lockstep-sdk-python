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
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel

@dataclass
class CustomFieldValueModel:
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
    recordKey: str | None = None
    stringValue: str | None = None
    numericValue: float | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    value: str | None = None
    customFieldDefinition: CustomFieldDefinitionModel | None = None

