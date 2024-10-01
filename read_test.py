import read_LaTeX as read

def test_read_document_from_text():
    text = r"""
    \begin{document}
    \section{Introduction}
    This is the introduction.
    \section{Conclusion}
    This is the conclusion.
    \\end{document}
    """
    document, _ = read.parse_document(text)
    print(document.children)

def main():
    test_read_document_from_text()

if __name__ == "__main__":
    main()