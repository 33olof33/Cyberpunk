from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db.base_class import BaseClass
from app.utils.repeater import repeats
from fastapi.logger import logger
from app import schemas
from app.core.config import settings
# from .test_data_processor import TestUsersProcessor
from . import requests


# @repeats(
#     amount=3,
#     delay=10,
#     message="Could not init database",
#     logger=logger,
#     error_type=ConnectionError,
# )
def init_db(db: Session, assets_dir: Optional[str] = None) -> None:
    from app import crud

    try:
        BaseClass.metadata.create_all(bind=db.bind)
        if crud.user.get_by_nickname(db, nickname=settings.ADMIN_NAME) is None:
            logger.info(
                "Creating new admin user, "
                f"as no existing with {settings.ADMIN_NAME} was found"
            )
            crud.user.create(
                db,
                obj_in=schemas.UserCreateAdmin(
                    email=settings.ADMIN_MAIL,
                    nickname=settings.ADMIN_NAME,
                    password=settings.ADMIN_PASSWORD,
                ),
            )

        # if settings.LOAD_TEST_CLIENTS and crud.user.length(db) <= 1:
        #     TestUsersProcessor(db).process("app/assets/test_data.json")

    except SQLAlchemyError:
        db.rollback()
        raise
