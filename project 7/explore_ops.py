import importlib


def explore_module():
    name = input("Enter module name to explore: ")
    try:
        module = importlib.import_module(name)
        attrs = [item for item in dir(module) if not item.startswith("__")]
        preview = attrs[:10]
        print(f"Available Attributes in {name} module:")
        print(f"{preview} ...]" if len(attrs) > 10 else preview)
    except ImportError:
        print(f"Could not find a module named '{name}'.")


def run_explore_menu():
    print("\nExplore Module Attributes:")
    explore_module()
    print("=" * 27)


if __name__ == "__main__":
    run_explore_menu()
