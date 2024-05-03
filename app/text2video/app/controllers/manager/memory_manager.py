from queue import Queue
from typing import Dict

from app.text2video.app.controllers.manager.base_manager import TaskManager  # 导入基类 TaskManager

class InMemoryTaskManager(TaskManager):  # 继承自 TaskManager 类
    def create_queue(self):
        # 实现 create_queue 方法，创建一个 Queue 对象作为任务队列
        return Queue()

    def enqueue(self, task: Dict):
        # 实现 enqueue 方法，将任务（字典类型）添加到队列中
        self.queue.put(task)

    def dequeue(self):
        # 实现 dequeue 方法，从队列中移除并返回一个任务
        return self.queue.get()

    def is_queue_empty(self):
        # 实现 is_queue_empty 方法，检查队列是否为空
        return self.queue.empty()