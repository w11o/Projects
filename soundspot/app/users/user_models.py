from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base, str_uniq, int_pk, str_null_true



class User(Base):
    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    password: Mapped[str]
    email: Mapped[str_uniq]
    spec_id: Mapped[int]

    spec: Mapped["Specializes"] = relationship("Specializes", back_populates="User")


    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email
        }


class Admin(Base):
    id: Mapped[int_pk]
    username: Mapped[str_uniq]
    password: Mapped[str]
    email: Mapped[str_uniq]
    role: Mapped[str]


    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)


class Specializes(Base):
    speciality_id:  Mapped[int_pk]
    speciality_name: Mapped[str]

    users: Mapped[list["User"]] = relationship("User", back_populates="Specializes")