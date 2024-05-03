import threading
from typing import Callable, Any, Dict

class TaskManager:
    def __init__(self, max_concurrent_tasks: int):
        # 初始化最大并发任务数
        self.max_concurrent_tasks = max_concurrent_tasks
        # 当前正在执行的任务数
        self.current_tasks = 0
        # 创建线程锁，用于同步线程间的操作
        self.lock = threading.Lock()
        # 创建任务队列，具体实现由子类完成
        self.queue = self.create_queue()

    def create_queue(self):
        # 应由子类实现以创建任务队列
        raise NotImplementedError()

    def add_task(self, func: Callable, *args: Any, **kwargs: Any):
        # 将任务添加到队列或立即执行
        with self.lock:
            if self.current_tasks < self.max_concurrent_tasks:
                print(f"add task: {func.__name__}, current_tasks: {self.current_tasks}")
                # 如果任务数小于最大并发数，立即执行任务
                self.execute_task(func, *args, **kwargs)
            else:
                print(f"enqueue task: {func.__name__}, current_tasks: {self.current_tasks}")
                # 如果任务数等于最大并发数，将任务加入队列
                self.enqueue({"func": func, "args": args, "kwargs": kwargs})

    def execute_task(self, func: Callable, *args: Any, **kwargs: Any):
        # 创建一个新线程来执行任务
        thread = threading.Thread(target=self.run_task, args=(func, *args), kwargs=kwargs)
        thread.start()

    def run_task(self, func: Callable, *args: Any, **kwargs: Any):
        try:
            with self.lock:
                # 任务开始时增加当前任务数
                self.current_tasks += 1
            # 调用函数，传递*args和**kwargs
            func(*args, **kwargs)
        finally:
            # 无论任务执行成功或失败，任务完成后调用task_done
            self.task_done()

    def check_queue(self):
        # 检查队列并执行队列中的任务（如果当前任务数小于最大并发数）
        with self.lock:
            if self.current_tasks < self.max_concurrent_tasks and not self.is_queue_empty():
                task_info = self.dequeue()
                func = task_info['func']
                args = task_info.get('args', ())
                kwargs = task_info.get('kwargs', {})
                # 执行队列中的下一个任务
                self.execute_task(func, *args, **kwargs)

    def task_done(self):
        # 任务完成时减少当前任务数并检查队列
        with self.lock:
            self.current_tasks -= 1
        self.check_queue()

    def enqueue(self, task: Dict):
        # 应由子类实现以将任务加入队列
        raise NotImplementedError()

    def dequeue(self):
        # 应由子类实现以从队列中取出任务
        raise NotImplementedError()

    def is_queue_empty(self):
        # 应由子类实现以检查队列是否为空
        raise NotImplementedError()