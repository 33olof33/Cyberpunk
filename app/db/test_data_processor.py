# import abc
# import json
# import random
# from uuid import UUID
# from typing import Union, Literal
#
# from sqlalchemy.orm.session import Session
# from pydantic import BaseModel
# from app import schemas
# from app.core.config import settings
#
#
# class TestDataProcessor(abc.ABC):
#     @abc.abstractmethod
#     def process(self, filename: str) -> None: ...
#
#
# class CustomerDataSchema(schemas.CustomerCreate):
#     plants: list[schemas.PlantCreate] = []
#
#
# class PartnerDataSchema(schemas.PartnerCreate):
#     elc_partner_id: Union[UUID, Literal["random"]]
#     workers: list[schemas.UserCreate] = []
#     customers: list[CustomerDataSchema] = []
#
#
# class OwnerSchema(BaseModel):
#     user_data: schemas.UserCreate
#     partner_data: PartnerDataSchema
#
#
# class ContentSchema(BaseModel):
#     clients: list[OwnerSchema]
#
#
# class TestUsersProcessor(TestDataProcessor):
#     def __init__(self, db: Session) -> None:
#         self.db = db
#
#     def process(self, filename: str) -> None:
#         from app import crud
#
#         with open(filename) as file:
#             data = ContentSchema(**json.load(file))
#
#         with crud.using(self.db):
#             admin = crud.user.get_by_email(email=settings.ADMIN_MAIL)
#             assert admin is not None
#
#             for client in data.clients:
#                 user = crud.user.create(
#                     obj_in=schemas.UserCreateAdmin(
#                         **client.user_data.dict(), is_admin=False, verified=True
#                     ),
#                 )
#                 if client.partner_data.elc_partner_id == "random":
#                     client.partner_data.elc_partner_id = random.choice(
#                         crud.elc_partner.get_multi().items
#                     ).id
#
#                 partner = crud.partner.create(
#                     obj_in=schemas.PartnerCreateExtended(
#                         owner_id=user.id, **client.partner_data.dict()
#                     ),
#                 )
#                 user.working_partner_id = partner.id
#                 self.db.commit()
#                 self.db.refresh(user)
#
#                 for worker in client.partner_data.workers:
#                     worker_user = crud.user.create(
#                         obj_in=schemas.UserCreateAdmin(
#                             **worker.dict(), is_admin=False, verified=True
#                         ),
#                     )
#                     worker_user.working_partner_id = partner.id
#                     self.db.commit()
#                     self.db.refresh(worker_user)
#
#                 for customer in client.partner_data.customers:
#                     customer_obj = crud.customer.create(
#                         obj_in=schemas.CustomerCreateExtended(
#                             **customer.dict(), partner_id=partner.id
#                         )
#                     )
#
#                     for plant in customer.plants:
#                         plant_obj = crud.plant.create(
#                             obj_in=schemas.PlantCreateExtended(
#                                 **plant.dict(), customer_id=customer_obj.id
#                             )
#                         )
#
#                         crud.plant_history.create(
#                             obj_in=schemas.PlantHistoryCreate(
#                                 message="Plant created by admin",
#                                 args=[admin.id],
#                                 plant_id=plant_obj.id,
#                             )
#                         )
