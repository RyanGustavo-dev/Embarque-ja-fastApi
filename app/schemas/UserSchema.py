from pydantic import EmailStr, BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    telefone: str
    url_imagem: str
    logo_sidebar: str
    biografia: str

class UserResponse(UserBase):
    id: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    url_imagem: Optional[str] = None
    logo_sidebar: Optional[str] = None
    biografia: Optional[str] = None

