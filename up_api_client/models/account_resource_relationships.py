from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_resource_relationships_transactions import (
        AccountResourceRelationshipsTransactions,
    )


T = TypeVar("T", bound="AccountResourceRelationships")


@_attrs_define
class AccountResourceRelationships:
    """
    Attributes:
        transactions (AccountResourceRelationshipsTransactions):
    """

    transactions: "AccountResourceRelationshipsTransactions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions = self.transactions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.account_resource_relationships_transactions import (
            AccountResourceRelationshipsTransactions,
        )

        d = src_dict.copy()
        transactions = AccountResourceRelationshipsTransactions.from_dict(
            d.pop("transactions")
        )

        account_resource_relationships = cls(
            transactions=transactions,
        )

        account_resource_relationships.additional_properties = d
        return account_resource_relationships

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
