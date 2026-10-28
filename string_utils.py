def normalize_string(text):
    """
    Chuẩn hóa khoảng trắng trong chuỗi.

    Input: một chuỗi ký tự.
    Output: chuỗi đã bỏ khoảng trắng thừa.
    """
    return " ".join(text.split())


if __name__ == "__main__":
    sample = "  Hello    Git   World  "
    result = normalize_string(sample)

    print(f"Input:  {sample!r}")
    print(f"Output: {result!r}")
