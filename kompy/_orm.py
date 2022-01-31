# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Index, Integer, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Db3Master(Base):
    __tablename__ = 'db3_master'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    version = Column(Integer, nullable=False)
    min_write_version = Column(Integer, nullable=False)
    min_read_version = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=False, server_default=text("0"))
    updated_at = Column(Integer, nullable=False, server_default=text("0"))


class KBankChain(Base):
    __tablename__ = 'k_bank_chain'
    __table_args__ = (
        UniqueConstraint('bcvendor', 'entry1', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    bcvendor = Column(Text)
    entry1 = Column(Text, nullable=False)
    entry2 = Column(Text)
    entry3 = Column(Text)


class KCategory(Base):
    __tablename__ = 'k_category'
    __table_args__ = (
        UniqueConstraint('category', 'subcategory', 'subsubcategory'),
    )

    id = Column(Integer, primary_key=True)
    category = Column(Text)
    subcategory = Column(Text)
    subsubcategory = Column(Text)

    sound_infos = relationship('KSoundInfo', secondary='k_sound_info_category')


class KContentPath(Base):
    __tablename__ = 'k_content_path'
    __table_args__ = (
        Index('index_content_path_visible', 'visible', 'content_type'),
    )

    id = Column(Integer, primary_key=True)
    path = Column(Text, nullable=False, unique=True)
    content_type = Column(Integer, nullable=False, server_default=text("0"))
    alias = Column(Text)
    state = Column(Integer, nullable=False, server_default=text("0"))
    scanned_at = Column(Integer, nullable=False, server_default=text("0"))
    product_id = Column(Text)
    product_version = Column(Integer)
    updated_at = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(Integer, nullable=False, server_default=text("0"))
    visible = Column(Integer, nullable=False, server_default=text("1"))
    upid = Column(Text)
    monitored = Column(Integer, nullable=False, server_default=text("0"))


class KMode(Base):
    __tablename__ = 'k_mode'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

    sound_infos = relationship('KSoundInfo', secondary='k_sound_info_mode')


class PSoundInfoEffect1(Base):
    __tablename__ = 'p_sound_info_Effect_1'
    __table_args__ = (
        Index('index_p_sound_info_Effect_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoEffect2(Base):
    __tablename__ = 'p_sound_info_Effect_2'
    __table_args__ = (
        Index('index_p_sound_info_Effect_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoGroup1(Base):
    __tablename__ = 'p_sound_info_Group_1'
    __table_args__ = (
        Index('index_p_sound_info_Group_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoGroup2(Base):
    __tablename__ = 'p_sound_info_Group_2'
    __table_args__ = (
        Index('index_p_sound_info_Group_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoInstrument1(Base):
    __tablename__ = 'p_sound_info_Instrument_1'
    __table_args__ = (
        Index('index_p_sound_info_Instrument_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoInstrument2(Base):
    __tablename__ = 'p_sound_info_Instrument_2'
    __table_args__ = (
        Index('index_p_sound_info_Instrument_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoLoop1(Base):
    __tablename__ = 'p_sound_info_Loop_1'
    __table_args__ = (
        Index('index_p_sound_info_Loop_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoLoop2(Base):
    __tablename__ = 'p_sound_info_Loop_2'
    __table_args__ = (
        Index('index_p_sound_info_Loop_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoOneshot1(Base):
    __tablename__ = 'p_sound_info_Oneshot_1'
    __table_args__ = (
        Index('index_p_sound_info_Oneshot_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoOneshot2(Base):
    __tablename__ = 'p_sound_info_Oneshot_2'
    __table_args__ = (
        Index('index_p_sound_info_Oneshot_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoProject1(Base):
    __tablename__ = 'p_sound_info_Project_1'
    __table_args__ = (
        Index('index_p_sound_info_Project_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoProject2(Base):
    __tablename__ = 'p_sound_info_Project_2'
    __table_args__ = (
        Index('index_p_sound_info_Project_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoSound1(Base):
    __tablename__ = 'p_sound_info_Sound_1'
    __table_args__ = (
        Index('index_p_sound_info_Sound_1_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


class PSoundInfoSound2(Base):
    __tablename__ = 'p_sound_info_Sound_2'
    __table_args__ = (
        Index('index_p_sound_info_Sound_2_bcs', 'entry1', 'bcvendor', 'entry2', 'entry3'),
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False, index=True)
    author = Column(Text)
    vendor = Column(Text)
    bank_chain_id = Column(Integer)
    entry1 = Column(Text)
    entry2 = Column(Text)
    entry3 = Column(Text)
    bcvendor = Column(Text)
    content_path_id = Column(Integer, nullable=False)
    favorite_id = Column(Text, index=True)


t_sqlite_stat1 = Table(
    'sqlite_stat1', metadata,
    Column('tbl', NullType),
    Column('idx', NullType),
    Column('stat', NullType)
)


t_sqlite_stat4 = Table(
    'sqlite_stat4', metadata,
    Column('tbl', NullType),
    Column('idx', NullType),
    Column('neq', NullType),
    Column('nlt', NullType),
    Column('ndlt', NullType),
    Column('sample', NullType)
)


class KSoundInfo(Base):
    __tablename__ = 'k_sound_info'
    __table_args__ = (
        UniqueConstraint('file_name', 'uuid'),
        Index('index_sound_info_content_path', 'content_path_id', 'file_ext'),
        Index('index_sound_info_bank_chain', 'bank_chain_id', 'content_path_id', 'file_ext')
    )

    id = Column(Integer, primary_key=True)
    version = Column(Integer)
    name = Column(Text, nullable=False)
    author = Column(Text)
    comment = Column(Text)
    vendor = Column(Text)
    color = Column(Integer, nullable=False, server_default=text("0"))
    tempo = Column(Float, nullable=False, server_default=text("0"))
    device_type_flags = Column(Integer, nullable=False, server_default=text("0"))
    bank_chain_id = Column(ForeignKey('k_bank_chain.id'))
    content_path_id = Column(ForeignKey('k_content_path.id'), nullable=False)
    file_name = Column(Text, nullable=False)
    file_ext = Column(Text)
    uuid = Column(Text)
    file_size = Column(Integer, nullable=False, server_default=text("0"))
    mod_date = Column(Integer, nullable=False, server_default=text("0"))
    updated_at = Column(Integer, nullable=False, server_default=text("0"))
    created_at = Column(Integer, nullable=False, server_default=text("0"))
    hidden_for = Column(Integer, nullable=False, server_default=text("0"))
    virtualBC = Column(Integer, nullable=False, server_default=text("0"))
    favorite_id = Column(Text, index=True)

    bank_chain = relationship('KBankChain')
    content_path = relationship('KContentPath')


t_k_sound_info_category = Table(
    'k_sound_info_category', metadata,
    Column('sound_info_id', ForeignKey('k_sound_info.id'), primary_key=True, nullable=False),
    Column('category_id', ForeignKey('k_category.id'), primary_key=True, nullable=False),
    Index('index_sound_info_category_2', 'category_id', 'sound_info_id', unique=True)
)


t_k_sound_info_mode = Table(
    'k_sound_info_mode', metadata,
    Column('sound_info_id', ForeignKey('k_sound_info.id'), primary_key=True, nullable=False),
    Column('mode_id', ForeignKey('k_mode.id'), primary_key=True, nullable=False),
    Index('index_sound_info_mode_2', 'mode_id', 'sound_info_id', unique=True)
)
