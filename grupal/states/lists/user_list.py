import reflex as rx


class UserListState(rx.State):
    list_filter: str = None

    def get_list_filter(self) -> str:
        return self.list_filter

    def set_list_filter(self, filter_param: str):
        self.list_filter = filter_param
