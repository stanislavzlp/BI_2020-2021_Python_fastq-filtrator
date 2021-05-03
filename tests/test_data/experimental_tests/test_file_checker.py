from tests.test_data.experimental_tests.file_creator import create_file


def test_create_file():
    file_name = 'gvadelupa'
    text = 'pipos'
    create_file(file_name, text)
    assert file_name.read_text() == text
