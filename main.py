from src.pdf_reader import extract_text

def main():
    pdf_path = "sample_papers/Attention Is All You Need.pdf"

    text = extract_text(pdf_path)

    print(text[:1000])


if __name__ == "__main__":
    main()