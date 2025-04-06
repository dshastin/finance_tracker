from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
from db.mixins import CreatedUpdatedMixin


class Stock(CreatedUpdatedMixin, Base):
    """Stocks table."""

    __table_name__ = 'stocks'


    secid: Mapped[str] = mapped_column(String(51), nullable=False)
    boardid: Mapped[str] = mapped_column(String(12), nullable=False)
    title: Mapped[str] = mapped_column(String(381), nullable=False)
    board_group_id: Mapped[int] = mapped_column(Integer, nullable=False)
    market_id: Mapped[int] = mapped_column(Integer, nullable=False)
    market: Mapped[str] = mapped_column(String(45), nullable=False)
    engine_id: Mapped[int] = mapped_column(Integer, nullable=False)
    engine: Mapped[str] = mapped_column(String(45), nullable=False)
    is_traded: Mapped[int] = mapped_column(Integer, nullable=False)
    decimals: Mapped[int] = mapped_column(Integer, nullable=False)
    history_from: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    history_till: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    listed_from: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    listed_till: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_primary: Mapped[int] = mapped_column(Integer, nullable=False)
    currencyid: Mapped[str] = mapped_column(String(9), nullable=False)
    unit: Mapped[str] = mapped_column(String(3), nullable=False)
