from office365.directory.identitySet import IdentitySet
from office365.entity import Entity
from office365.onedrive.itemReference import ItemReference
from office365.runtime.queries.delete_entity_query import DeleteEntityQuery


class BaseItem(Entity):
    """The baseItem resource is an abstract resource that contains a common set of properties shared among several
    other resources types """

    def delete_object(self):
        """Deletes the item."""
        qry = DeleteEntityQuery(self)
        self.context.add_query(qry)
        self.remove_from_parent_collection()
        return self

    @property
    def etag(self):
        """ETag for the item."""
        if self.is_property_available("eTag"):
            return self.properties['eTag']
        return None

    @property
    def createdBy(self):
        """Identity of the user, device, or application which created the item."""
        return self.properties.get('createdBy', IdentitySet())

    @property
    def lastModifiedBy(self):
        """Identity of the user, device, and application which last modified the item."""
        if self.is_property_available("lastModifiedBy"):
            return self.properties['lastModifiedBy']
        return IdentitySet()

    @property
    def createdDateTime(self):
        """Date and time of item creation."""
        if self.is_property_available("createdDateTime"):
            return self.properties['createdDateTime']
        return None

    @property
    def lastModifiedDateTime(self):
        """Date and time the item was last modified."""
        if self.is_property_available("lastModifiedDateTime"):
            return self.properties['lastModifiedDateTime']
        return None

    @property
    def name(self):
        """The name of the item."""
        return self.properties.get('name', None)

    @name.setter
    def name(self, value):
        self.properties['name'] = value

    @property
    def description(self):
        """Provides a user-visible description of the item."""
        if self.is_property_available("description"):
            return self.properties['description']
        return None

    @description.setter
    def description(self, value):
        self.properties['description'] = value

    @property
    def web_url(self):
        """URL that displays the resource in the browser."""
        if self.is_property_available("webUrl"):
            return self.properties['webUrl']
        return None

    @property
    def parentReference(self):
        """Parent information, if the item has a parent."""
        return self.properties.get('parentReference', ItemReference())

    @parentReference.setter
    def parentReference(self, value):
        self.properties['parentReference'] = value
