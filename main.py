from database.db import init_db


def main():
    print("Initializing Job Application Assistant...")

    init_db()

    print("Database initialized successfully.")
    print("System ready.")


if __name__ == "__main__":
    main()