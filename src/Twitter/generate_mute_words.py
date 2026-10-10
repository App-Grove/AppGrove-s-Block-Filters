# generate_mute_words.py

# 必要なライブラリをインポート
import re


class GenerateMuteWords:

    # 初期化メソッド
    def __init__(self, repo_root):
        self.REPO_ROOT = repo_root
        self.SRC = self.REPO_ROOT / "sources/Twitter/mute_words.src.txt"
        self.DIST = self.REPO_ROOT / "Twitter/mute_words.txt"
        self.FILTER_BASE = 'x.com##div[data-testid="cellInnerDiv"]:has-text(/{words}/)'
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
            if line.startswith("\\"):
                # バックスラッシュは「正規表現ではなく文字列」を示す印
                words.append(self._escape_literal(line[1:]))
            elif line.startswith("@"):
                # @以降は正規表現としてそのまま使用
                words.append(line[1:])

        self._append_filter(filters_lines, words)

        with open(self.DIST, "w", encoding="utf-8") as f:
            f.write("\n".join(filters_lines) + "\n")

    # 正規表現のリテラルとして安全に使用できる形にするメソッド
    def _escape_literal(self, word):
        # uBlock Originの正規表現区切り文字 / もエスケープする
        return re.sub(r"([.\\+*?^$()\[\]{}|/])", r"\\\1", word)

    # 単語をフィルターとして追加するメソッド
    def _append_filter(self, filters_lines, words):
        if words:
            filters_lines.append(self.FILTER_BASE.format(words="|".join(words)))
