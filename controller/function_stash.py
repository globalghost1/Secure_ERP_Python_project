from view import terminal as view


def update_logic(label, folder_name_update_function, headers, department_data):
    row_to_update = int(view.get_input(f"\nEnter a valid row number to edit "
                                       f"{label}'s data(e.g. 1): ")) - 1
    if len(department_data) > row_to_update >= 0:
        view.print_general_results(department_data[row_to_update], headers)
        column_index = view.print_message("\nWhich category would you like to edit:")
        for index, header in enumerate(headers, 1):
            if index == len(headers) - 1:
                view.print_message(f"{index}) {headers[index]}")
                break
            else:
                view.print_message(f"{index}) {headers[index]},")
        column_index = int(view.get_input(""))
        if 0 < column_index < len(headers):
            cell_update_content = view.get_input("\nEnter a new value for the selected category: ")
            update_confirmation = view.get_input(f"Are you sure you want to update {label}'s "
                                                 f"{headers[column_index]}: "
                                                 f"{department_data[row_to_update][column_index]} "
                                                 f"to {cell_update_content}? (y/n) ").lower()
            if update_confirmation.startswith("y"):
                folder_name_update_function(row_to_update, column_index, cell_update_content)
                view.print_message(f"\nSuccessfully updated data!\n"
                                   f"{headers[column_index]} "
                                   f"for row {row_to_update + 1} has been "
                                   f"changed to: {cell_update_content} ")
            else:
                view.print_message("\nNo data has been updated.")
        else:
            view.print_error_message("No such category in this table!")
    else:
        view.print_error_message(f"There is no such row ({row_to_update + 1}) in this table!")


def delete_logic(label, folder_name_delete_function, department_data):
    row_to_delete = int(view.get_input(f"\nEnter a valid row number to delete {label}'s data(e.g. 1): ")) - 1
    if len(department_data) > row_to_delete >= 0:
        delete_confirmation = view.get_input(f"\nAre you sure you want to delete this transaction: "
                                             f"{department_data[row_to_delete]}? (y/n) ").lower()
        if delete_confirmation.startswith("y"):
            folder_name_delete_function(row_to_delete)
            view.print_message(f"\nData from row {row_to_delete + 1} has been successfully removed!")
        else:
            view.print_message("\nNo data has been removed.")
    else:
        view.print_error_message(f"There isn't such a row ({row_to_delete + 1}) in this table!")
