from enum import Enum

class TypeMovement(Enum):
    """Enumeration of movement types."""
    farm = "farm"
    slaughterhouse = "slaughterhouse"
    municipality = "municipality"
    collection_center = "collection_center"
    cattle_fair = "cattle_fair"
    enterprise = "enterprise"