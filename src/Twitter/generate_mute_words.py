# generate_mute_words.py

class GenerateMuteWords:

    # 初期化メソッド
    def __init__(self, repo_root):
        self.REPO_ROOT = repo_root
        self.SRC = self.REPO_ROOT / "sources/Twitter/mute_words.src.txt"
        self.DIST = self.REPO_ROOT / "Twitter/mute_words.txt"
        self.FILTER_BASE = (
            'x.com##body:xpath(//div[@data-testid="cellInnerDiv" '
            'and .//span[{words}] '
            'and .//div[@data-testid="User-Name"]/div/div/'
            'a[@role="link" and not(@href=//a[@aria-label="プロフィール"]/@href)]])'
        )
        self.TITLE = "daizu's twitter mute words"
        self.HOMEPAGE = "https://github.com/App-Grove/AppGrove-s-Block-Filters"

    # 外部から実行するメソッド
    def run(self):
        self._ensure_file_exists()
        self._generate_mute_words()

    # 出力ファイルの存在を確約
    def _ensure_file_exists(self):
        if not self.DIST.exists():
            self.DIST.touch()

    # mute_words.src.txtを読み込み、mute_words.txtを生成するメソッド
    def _generate_mute_words(self):
        if not self.SRC.exists():
            print(f"{self.SRC} does not exist.")
            return

        with open(self.SRC, "r", encoding="utf-8") as f:
            source_lines = f.read().splitlines()
        if not source_lines:
            print(f"{self.SRC} is empty.")
            return

        filters_lines = [
            f"! Title: {self.TITLE}",
            f"! Homepage: {self.HOMEPAGE}",
            "",
        ]
        words = []

        for line in source_lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("!"):
                self._append_filter(filters_lines, words)
                words = []
                filters_lines.append(line)
                continue
            words.append(line)

        self._append_filter(filters_lines, words)

        with open(self.DIST, "w", encoding="utf-8") as f:
            f.write("\n".join(filters_lines) + "\n")

    # XPath 1.0の文字列リテラルを作成するメソッド
    def _xpath_literal(self, value):
        if '"' not in value:
            return f'"{value}"'
        if "'" not in value:
            return f"'{value}'"

        parts = value.split('"')
        arguments = []
        for index, part in enumerate(parts):
            if part:
                arguments.append(f'"{part}"')
            if index < len(parts) - 1:
                arguments.append("'\"'")
        return f"concat({','.join(arguments)})"

    # 単語をフィルターとして追加するメソッド
    def _append_filter(self, filters_lines, words):
        if words:
            word_conditions = " or ".join(
                f"contains(text(), {self._xpath_literal(word)})" for word in words
            )
            filters_lines.append(self.FILTER_BASE.format(words=word_conditions))
