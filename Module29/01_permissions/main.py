from typing import Callable


def check_permission(user: str) -> Callable:
    """
    Дероратор проверяет наличие прав пользователя
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                if user in user_permissions:
                    result = func(*args, **kwargs)
                else:
                    raise PermissionError
                return result
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()