#!/bin/bash

# Determine the directory of the script
script_directory=$(dirname "$(readlink -f "$0")")

# Relative path to JSON file containing state to AWS region mapping
mapping_file="$script_directory/state_regions.json"

while true; do
    # Prompt user for state input
    read -p "Enter state (type 'q' to quit): " state

    # Check if user wants to quit
    if [ "$state" == "q" ]; then
        echo "Exiting the script. Goodbye!"
        break
    fi

    # Fetch AWS region from the mapping file based on the provided state
    region=$(grep -o "\"$state\": *\"[^\"]*\"" "$mapping_file" | cut -d "\"" -f 4 2>/dev/null)

    # Check if the state is valid
    if [ -z "$region" ]; then
        echo "Invalid state. Please enter a valid state from the mapping file."
    else
        # Output the result in JSON format
        echo -e "{\n  \"state\": \"$state\",\n  \"region\": \"$region\"\n}"

        # Alternatively, you can output in YAML format (requires 'yq' tool)
        # echo -e "state: $state\nregion: $region" | yq eval - -j

        echo -e "\n"
    fi
done

