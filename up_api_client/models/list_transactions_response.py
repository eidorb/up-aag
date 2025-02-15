from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_transactions_response_links import ListTransactionsResponseLinks
    from ..models.transaction_resource import TransactionResource


T = TypeVar("T", bound="ListTransactionsResponse")


@_attrs_define
class ListTransactionsResponse:
    """Successful response to get all transactions. This returns a paginated
    list of transactions, which can be scrolled by following the `prev` and
    `next` links if present.

        Attributes:
            data (list['TransactionResource']): The list of transactions returned in this response.
            links (ListTransactionsResponseLinks):
    """

    data: list["TransactionResource"]
    links: "ListTransactionsResponseLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.list_transactions_response_links import (
            ListTransactionsResponseLinks,
        )
        from ..models.transaction_resource import TransactionResource

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TransactionResource.from_dict(data_item_data)

            data.append(data_item)

        links = ListTransactionsResponseLinks.from_dict(d.pop("links"))

        list_transactions_response = cls(
            data=data,
            links=links,
        )

        list_transactions_response.additional_properties = d
        return list_transactions_response

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
