from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Product quantity")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(CartItemBase):
    product_id: int=Field(..., description="Product ID")
    quantity: int=Field(..., gt=0, 
                        description="New Product quantity")

class CartItem(BaseModel):
    product_id:int
    name: str=Field(..., description="Product name")
    price: float=Field(..., gt=0, description="Product price")
    quantity: int=Field(..., gt=0, description="Product quantity in cart")
    subtotal: float=Field(...,  
                          description="Total prise for this item(prise * quantity)")
    image_url: Optional[str]=Field(None, description="Product image url")

class CartResponse(BaseModel):
    items: list[CartItem]=Field(..., description="List of cart items")
    total: float=Field(..., description="Total prise for all items in cart")
    items_count: int=Field(..., description="Total number of items in cart")
