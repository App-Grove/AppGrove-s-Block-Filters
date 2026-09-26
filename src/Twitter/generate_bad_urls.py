# generate_bad_urls.py

# 必要なライブラリをインポート
import re


class GenerateBadUrls:

    # 正規表現で特別な意味を持つ文字(ドメインを正規表現に埋め込むためエスケープが必要)
    REGEX_SPECIAL_CHARS = re.compile(r"([.\\+*?^$()\[\]{}|/])")

    # 初期化メソッド
    def __init__(self, repo_root):
        self.REPO_ROOT = repo_root
        self.SRC = self.REPO_ROOT / "sources/Twitter/bad_urls.src.txt"
        self.DIST = self.REPO_ROOT / "Twitter/bad_urls.txt"
        self.FILTER_BASE = 'x.com##div[data-testid="cellInnerDiv"]:has-text(/{urls}/)'
        self.TITLE = "Bad URLs for Twitter"
        self.HOMEPAGE = "https://github.com/App-Grove/AppGrove-s-Block-Filters"

    # 外部から実行するメソッド
    def run(self):
        self._ensure_file_exists()
        self._generate_bad_urls()

    # 出力ファイルの存在を確約
    def _ensure_file_exists(self):
        if not self.DIST.exists(): # ファイルがない場合は生成
            self.DIST.touch()

    # bad_urls.src.txtを読み込み、bad_urls.txtを生成するメソッド
    def _generate_bad_urls(self):
        # ヘッダーを追加
        filters_lines = [
            f"! Title: {self.TITLE}",
            f"! Homepage: {self.HOMEPAGE}",
            "",
        ]
        # bad_urls.src.txtが存在するか確認
        if not self.SRC.exists():
            print(f"{self.SRC} does not exist.")
            return
        # bad_urls.src.txtを読み込む
        with open(self.SRC, "r", encoding="utf-8") as f:
            bad_urls = f.read().splitlines()
        if not bad_urls:
            print(f"{self.SRC} is empty.")
            return
        # !から始まる行を区切りとして(コメント, URLのリスト)の組にまとめる
        groups = [] # グループを格納するリスト
        comment = None # 現在のグループのコメント
        urls = [] # 現在のグループのURLを一時的に格納するリスト
        seen = set() # 重複したURLを除外するためのセット
        for line in bad_urls:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"): # コメント行は無視
                continue
            if line.startswith("!"): # 区切りコメントの行
                if urls:
                    groups.append((comment, urls))
                comment = line
                urls = []
                continue
            url = self._escape_for_regex(line) # 正規表現として評価されるためエスケープする
            if url in seen: # 重複は無視
                continue
            seen.add(url)
            urls.append(url)
        # 残されたURLを追加
        if urls:
            groups.append((comment, urls))
        # グループごとにフィルターを追加
        for comment, urls in groups:
            if comment: # グループのコメントがあれば出力
                filters_lines.append(comment)
            url_list = "|".join(urls)
            filters_lines.append(self.FILTER_BASE.format(urls=url_list))
        # ファイルに書き込む
        with open(self.DIST, "w", encoding="utf-8") as f:
            f.write("\n".join(filters_lines) + "\n")

    # 正規表現で特別な意味を持つ文字をエスケープするメソッド
    def _escape_for_regex(self, url):
        return self.REGEX_SPECIAL_CHARS.sub(r"\\\1", url)
