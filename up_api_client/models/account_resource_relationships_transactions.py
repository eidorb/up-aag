from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_resource_relationships_transactions_links import (
        AccountResourceRelationshipsTransactionsLinks,
    )


T = TypeVar("T", bound="AccountResourceRelationshipsTransactions")


@_attrs_define
class AccountResourceRelationshipsTransactions:
    """
    Attributes:
        links (Union[Unset, AccountResourceRelationshipsTransactionsLinks]):
    """

    links: Union[Unset, "AccountResourceRelationshipsTransactionsLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.account_resource_relationships_transactions_links import (
            AccountResourceRelationshipsTransactionsLinks,
        )

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, AccountResourceRelationshipsTransactionsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AccountResourceRelationshipsTransactionsLinks.from_dict(_links)

        account_resource_relationships_transactions = cls(
            links=links,
        )

        account_resource_relationships_transactions.additional_properties = d
        return account_resource_relationships_transactions

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
