from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, TIME

from ..database import db
from ..mixins import CRUDModel

class Teplota(CRUDModel):
    __tablename__ = 'teplota'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    teplota = Column(Integer, nullable=False, index=True)
    cas_insertu = Column(TIME)