import uuid


def generate_uuid():
    print(f"Generated UUID: {uuid.uuid4()}")


def run_uuid_menu():
    print("\nGenerate Unique Identifiers:")
    generate_uuid()
    print("=" * 27)


if __name__ == "__main__":
    run_uuid_menu()
