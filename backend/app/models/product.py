from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"),nullable=False)
    category = relationship("Category", back_populates="products")
    image_url = Column(String)
    created_at = Column(String, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #updated_at = Column(String, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return f"Product(id={self.id}, price={self.price})"