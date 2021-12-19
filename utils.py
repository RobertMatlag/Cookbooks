def prepare_file_name(s: str) -> str:
    return s.lower().replace(".", "").replace(" ", "_")


if __name__ == "__main__":
    print(prepare_file_name("3. Matching Strings Using Shell Wildcard Patterns"))
