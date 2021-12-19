def prepare_file_name(s: str) -> str:
    return s.lower().replace(' ', '_')


if __name__ == "__main__":
    print(prepare_file_name('20 Combining Multiple Mappings into a Single Mapping'))
