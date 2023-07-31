#!/usr/bin/env python3
import subprocess

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as f:
        f.write(task + "\n")
    print(f"Added task: {task}")

def list_tasks():
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks in the to-do list.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks in the to-do list.")

def remove_task():
    list_tasks()
    task_number = input("Enter the task number to remove: ")
    try:
        task_number = int(task_number)
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
        if 1 <= task_number <= len(tasks):
            task_to_remove = tasks.pop(task_number - 1)
            with open("todo.txt", "w") as f:
                f.writelines(tasks)
            print(f"Removed task: {task_to_remove.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def clear_tasks():
    import os
    if os.path.exists("todo.txt"):
        os.remove("todo.txt")
        print("All tasks cleared.")
    else:
        print("No tasks in the to-do list.")

def get_action_choice():
    menu_prompt = """gum choose "Add Task" "List Tasks" "Remove Task" "Clear All Tasks" "Exit" """
    try:
        action_choice = subprocess.check_output(menu_prompt, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        action_choice = ""
    return action_choice


def main():
    while True:
        action_choice = get_action_choice()

        if action_choice == "Add Task":
            add_task()
        elif action_choice == "List Tasks":
            list_tasks()
        elif action_choice == "Remove Task":
            remove_task()
        elif action_choice == "Clear All Tasks":
            clear_tasks()
        elif action_choice == "Exit":
            print("Exiting the to-do list program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
