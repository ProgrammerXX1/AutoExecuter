from pydantic import BaseModel

# Валидация входящих данных для создания задачи
class TaskCreate(BaseModel):
    title: str

# Ответ для клиента
class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True
