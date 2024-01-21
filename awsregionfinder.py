import json

# JSON file containing state to AWS region mapping
mapping_file = "state_regions.json"

while True:
    # Prompt user for state input
    state = input("Enter state (type 'q' to quit): ")

    # Check if user wants to quit
    if state.lower() == 'q':
        print("Exiting the script. Goodbye!")
        break

    try:
        # Read the mapping file
        with open(mapping_file, 'r') as file:
            state_mapping = json.load(file)

        # Fetch AWS region from the mapping based on the provided state
        region = state_mapping.get(state)

        # Check if the state is valid
        if region is None:
            print("Invalid state. Please enter a valid state from the mapping file.")
        else:
            # Output the result in JSON format
            result = {
                "state": state,
                "region": region
            }
            print(json.dumps(result, indent=2))

            # Alternatively, you can output in YAML-like format
            # print(f"state: {state}\nregion: {region}")

            print("\n")

    except FileNotFoundError:
        print(f"Mapping file '{mapping_file}' not found. Please check the file path.")
        break
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{mapping_file}'. Please check the file format.")
        break

