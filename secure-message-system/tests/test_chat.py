from src.chat import demo_chat


def test_demo_chat():
    result = demo_chat()

    assert result == "Hello Bob, secure channel established"