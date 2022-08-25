from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship


Base = declarative_base()




class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
    tasks = relationship(
        "Task", back_populates="group", cascade="all, delete"
    )


    def __repr__(self):
        return f"<Group(id={self.id}, name='{self.name}')>"


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    text = Column(String(255))

    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)


    def __repr__(self):
        return f"<Group(id={self.id}, title='{self.title}', text='{self.text}')>"


def get_session(connection_url="sqlite:///database.db"):
    engine = create_engine(connection_url)
    session = Session(engine)
    Base.metadata.create_all(engine)

    return session



