import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.transaction_status_enum import TransactionStatusEnum

if TYPE_CHECKING:
    from ..models.card_purchase_method_object import CardPurchaseMethodObject
    from ..models.cashback_object import CashbackObject
    from ..models.customer_object import CustomerObject
    from ..models.hold_info_object import HoldInfoObject
    from ..models.money_object import MoneyObject
    from ..models.note_object import NoteObject
    from ..models.round_up_object import RoundUpObject


T = TypeVar("T", bound="TransactionResourceAttributes")


@_attrs_define
class TransactionResourceAttributes:
    """
    Attributes:
        status (TransactionStatusEnum): Specifies which stage of processing a transaction is currently at.
            Currently returned values are `HELD` and `SETTLED`. When a transaction is
            held, its account’s `availableBalance` is affected. When a transaction is
            settled, its account’s `currentBalance` is affected.
        raw_text (Union[None, str]): The original, unprocessed text of the transaction. This is often not
            a perfect indicator of the actual merchant, but it is useful for
            reconciliation purposes in some cases.
        description (str): A short description for this transaction. Usually the merchant name
            for purchases.
        message (Union[None, str]): Attached message for this transaction, such as a payment message, or a
            transfer note.
        is_categorizable (bool): Boolean flag set to true on transactions that support the use of
            categories.
        hold_info (Union['HoldInfoObject', None]): If this transaction is currently in the `HELD` status, or was ever in
            the `HELD` status, the `amount` and `foreignAmount` of the
            transaction while `HELD`.
        round_up (Union['RoundUpObject', None]): Details of how this transaction was rounded-up. If no Round Up was
            applied this field will be `null`.
        cashback (Union['CashbackObject', None]): If all or part of this transaction was instantly reimbursed in the
            form of cashback, details of the reimbursement.
        amount (MoneyObject): Provides information about a value of money.
        foreign_amount (Union['MoneyObject', None]): The foreign currency amount of this transaction. This field will be
            `null` for domestic transactions. The amount was converted to the AUD
            amount reflected in the `amount` of this transaction. Refer to the
            `holdInfo` field for the original `foreignAmount` the transaction was
            `HELD` at.
        card_purchase_method (Union['CardPurchaseMethodObject', None]): Information about the card used for this
            transaction, if applicable.
        settled_at (Union[None, datetime.datetime]): The date-time at which this transaction settled. This field will be
            `null` for transactions that are currently in the `HELD` status.
        created_at (datetime.datetime): The date-time at which this transaction was first encountered.
        transaction_type (Union[None, str]): A description of the transaction method used e.g. Purchase, BPAY Payment.
        note (Union['NoteObject', None]): A customer provided note about the transaction.  Can only be provided by Up
            High subscribers.
        performing_customer (Union['CustomerObject', None]): The customer who initated the transaction.  For 2Up
            accounts this could be the customer who's card was used.
    """

    status: TransactionStatusEnum
    raw_text: Union[None, str]
    description: str
    message: Union[None, str]
    is_categorizable: bool
    hold_info: Union["HoldInfoObject", None]
    round_up: Union["RoundUpObject", None]
    cashback: Union["CashbackObject", None]
    amount: "MoneyObject"
    foreign_amount: Union["MoneyObject", None]
    card_purchase_method: Union["CardPurchaseMethodObject", None]
    settled_at: Union[None, datetime.datetime]
    created_at: datetime.datetime
    transaction_type: Union[None, str]
    note: Union["NoteObject", None]
    performing_customer: Union["CustomerObject", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.card_purchase_method_object import CardPurchaseMethodObject
        from ..models.cashback_object import CashbackObject
        from ..models.customer_object import CustomerObject
        from ..models.hold_info_object import HoldInfoObject
        from ..models.money_object import MoneyObject
        from ..models.note_object import NoteObject
        from ..models.round_up_object import RoundUpObject

        status = self.status.value

        raw_text: Union[None, str]
        raw_text = self.raw_text

        description = self.description

        message: Union[None, str]
        message = self.message

        is_categorizable = self.is_categorizable

        hold_info: Union[None, dict[str, Any]]
        if isinstance(self.hold_info, HoldInfoObject):
            hold_info = self.hold_info.to_dict()
        else:
            hold_info = self.hold_info

        round_up: Union[None, dict[str, Any]]
        if isinstance(self.round_up, RoundUpObject):
            round_up = self.round_up.to_dict()
        else:
            round_up = self.round_up

        cashback: Union[None, dict[str, Any]]
        if isinstance(self.cashback, CashbackObject):
            cashback = self.cashback.to_dict()
        else:
            cashback = self.cashback

        amount = self.amount.to_dict()

        foreign_amount: Union[None, dict[str, Any]]
        if isinstance(self.foreign_amount, MoneyObject):
            foreign_amount = self.foreign_amount.to_dict()
        else:
            foreign_amount = self.foreign_amount

        card_purchase_method: Union[None, dict[str, Any]]
        if isinstance(self.card_purchase_method, CardPurchaseMethodObject):
            card_purchase_method = self.card_purchase_method.to_dict()
        else:
            card_purchase_method = self.card_purchase_method

        settled_at: Union[None, str]
        if isinstance(self.settled_at, datetime.datetime):
            settled_at = self.settled_at.isoformat()
        else:
            settled_at = self.settled_at

        created_at = self.created_at.isoformat()

        transaction_type: Union[None, str]
        transaction_type = self.transaction_type

        note: Union[None, dict[str, Any]]
        if isinstance(self.note, NoteObject):
            note = self.note.to_dict()
        else:
            note = self.note

        performing_customer: Union[None, dict[str, Any]]
        if isinstance(self.performing_customer, CustomerObject):
            performing_customer = self.performing_customer.to_dict()
        else:
            performing_customer = self.performing_customer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "rawText": raw_text,
                "description": description,
                "message": message,
                "isCategorizable": is_categorizable,
                "holdInfo": hold_info,
                "roundUp": round_up,
                "cashback": cashback,
                "amount": amount,
                "foreignAmount": foreign_amount,
                "cardPurchaseMethod": card_purchase_method,
                "settledAt": settled_at,
                "createdAt": created_at,
                "transactionType": transaction_type,
                "note": note,
                "performingCustomer": performing_customer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.card_purchase_method_object import CardPurchaseMethodObject
        from ..models.cashback_object import CashbackObject
        from ..models.customer_object import CustomerObject
        from ..models.hold_info_object import HoldInfoObject
        from ..models.money_object import MoneyObject
        from ..models.note_object import NoteObject
        from ..models.round_up_object import RoundUpObject

        d = src_dict.copy()
        status = TransactionStatusEnum(d.pop("status"))

        def _parse_raw_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        raw_text = _parse_raw_text(d.pop("rawText"))

        description = d.pop("description")

        def _parse_message(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        message = _parse_message(d.pop("message"))

        is_categorizable = d.pop("isCategorizable")

        def _parse_hold_info(data: object) -> Union["HoldInfoObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hold_info_type_1 = HoldInfoObject.from_dict(data)

                return hold_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["HoldInfoObject", None], data)

        hold_info = _parse_hold_info(d.pop("holdInfo"))

        def _parse_round_up(data: object) -> Union["RoundUpObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                round_up_type_1 = RoundUpObject.from_dict(data)

                return round_up_type_1
            except:  # noqa: E722
                pass
            return cast(Union["RoundUpObject", None], data)

        round_up = _parse_round_up(d.pop("roundUp"))

        def _parse_cashback(data: object) -> Union["CashbackObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cashback_type_1 = CashbackObject.from_dict(data)

                return cashback_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CashbackObject", None], data)

        cashback = _parse_cashback(d.pop("cashback"))

        amount = MoneyObject.from_dict(d.pop("amount"))

        def _parse_foreign_amount(data: object) -> Union["MoneyObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                foreign_amount_type_1 = MoneyObject.from_dict(data)

                return foreign_amount_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MoneyObject", None], data)

        foreign_amount = _parse_foreign_amount(d.pop("foreignAmount"))

        def _parse_card_purchase_method(
            data: object,
        ) -> Union["CardPurchaseMethodObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                card_purchase_method_type_1 = CardPurchaseMethodObject.from_dict(data)

                return card_purchase_method_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CardPurchaseMethodObject", None], data)

        card_purchase_method = _parse_card_purchase_method(d.pop("cardPurchaseMethod"))

        def _parse_settled_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                settled_at_type_0 = isoparse(data)

                return settled_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        settled_at = _parse_settled_at(d.pop("settledAt"))

        created_at = isoparse(d.pop("createdAt"))

        def _parse_transaction_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        transaction_type = _parse_transaction_type(d.pop("transactionType"))

        def _parse_note(data: object) -> Union["NoteObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                note_type_1 = NoteObject.from_dict(data)

                return note_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NoteObject", None], data)

        note = _parse_note(d.pop("note"))

        def _parse_performing_customer(data: object) -> Union["CustomerObject", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                performing_customer_type_1 = CustomerObject.from_dict(data)

                return performing_customer_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CustomerObject", None], data)

        performing_customer = _parse_performing_customer(d.pop("performingCustomer"))

        transaction_resource_attributes = cls(
            status=status,
            raw_text=raw_text,
            description=description,
            message=message,
            is_categorizable=is_categorizable,
            hold_info=hold_info,
            round_up=round_up,
            cashback=cashback,
            amount=amount,
            foreign_amount=foreign_amount,
            card_purchase_method=card_purchase_method,
            settled_at=settled_at,
            created_at=created_at,
            transaction_type=transaction_type,
            note=note,
            performing_customer=performing_customer,
        )

        transaction_resource_attributes.additional_properties = d
        return transaction_resource_attributes

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
