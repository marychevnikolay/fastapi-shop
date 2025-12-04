from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductResponse(BaseModel):
    
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0,
                       description="Product price(must be greater than 0)")
    
    category_id: int = Field(..., description="Category ID")
    # category: CategoryResponse = Field(..., description="Product category")
    image_url: Optional[str] = Field(None, description="Product image url")
    # created_at: datetime = Field(..., description="Product creation date")

class ProductCreate(ProductResponse):
    pass

class ProducResponse(ProductResponse):
    id: int= Field(..., description="Unique product id")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse= Field(..., description="Product category")


    class Config:
        form_attribute = True

class ProductListResponse(BaseModel):
    products: list[ProducResponse]
    total: int= Field(..., description="Total number of products")