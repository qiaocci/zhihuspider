import sys

sys.path.append(".")
sys.path.append("..")
from tasks import execute_user_task  # noqa isort:skip


if __name__ == "__main__":
    execute_user_task()
