from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, text)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
    conn.commit()


metadata_obj = MetaData()

user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)
