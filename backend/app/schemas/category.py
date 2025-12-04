from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=10,
                      description="Category name")
    
    slug: str= Field(..., min_length=3, max_length=10,
                      description="URL frendly category name")
    #description: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int= Field(..., description="Unique category id")

    class Config:
        form_attribute = True