import os
import requests


def load_api_key():
    api_key_file = "api_key.txt"
    if os.path.exists(api_key_file):
        with open(api_key_file, 'r') as file:
            return file.read().strip()
    else:
        return None


def save_api_key(api_key):
    api_key_file = "api_key.txt"
    with open(api_key_file, 'w') as file:
        file.write(api_key)


def make_request(term, func, api_key):
    url = "https://breachdirectory.p.rapidapi.com/"
    querystring = {"func": func, "term": term}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def write_to_file(result, file_path):
    with open(file_path, 'a') as file:
        file.write("\n\n")
        for key, value in result.items():
            if isinstance(value, list):
                file.write(f"{key}:\n")
                for item in value:
                    file.write(f"  {item}\n")
            else:
                file.write(f"{key}: {value}\n")


def main():
    api_key = load_api_key()

    if not api_key:
        api_key = input("Enter your API key: ")
        save_api_key(api_key)

    email = input("Enter the email or term to check for breaches: ")
    func = input("Enter the function (auto, hashes, sources, password, domain, dehash): ")
    output_file = input("Enter the path to the output text file: ")

    result = make_request(email, func, api_key)
    write_to_file(result, output_file)


if __name__ == "__main__":
    main()
