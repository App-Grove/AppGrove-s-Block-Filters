# generate_mute_users.py

# 必要なライブラリをインポート


class GenerateMuteUsers:

    # 初期化メソッド
    def __init__(self, repo_root):
        self.REPO_ROOT = repo_root
        self.SRC = self.REPO_ROOT / "sources/Twitter/mute_users.src.txt"
        self.DIST = self.REPO_ROOT / "Twitter/mute_users.txt"
        self.USER_BASE = '[href="/{name}"]'
        self.FILTER_BASE = 'x.com##div[style^="transform"][data-testid="cellInnerDiv"]:has(article[data-testid="tweet"] div[data-testid="User-Name"] a:is({users}))'
        self.TITLE = "daizu's twitter mute users"
        self.HOMEPAGE = "https://github.com/App-Grove/AppGrove-s-Block-Filters"

    # 外部から実行するメソッド
    def run(self):
        self._ensure_file_exists()
        self._generate_mute_users()

    # 出力ファイルの存在を確約
    def _ensure_file_exists(self):
        if not self.DIST.exists(): # ファイルがない場合は生成
            self.DIST.touch()

    # mute_users.src.txtを読み込み、mute_users.txtを生成するメソッド
    def _generate_mute_users(self):
        filters_lines = [] # フィルターを行ごとに格納するリスト
        users = [] # ユーザー名を一時的に格納するリスト
        # ヘッダーを追加
        filters_lines.append(f"! Title: {self.TITLE}")
        filters_lines.append(f"! Homepage: {self.HOMEPAGE}")
        # mute_users.src.txtが存在するか確認
        if not self.SRC.exists():
            print(f"{self.SRC} does not exist.")
            return
        # mute_users.src.txtを読み込む
        with open(self.SRC, "r", encoding="utf-8") as f:
            mute_users = f.read().splitlines()
            if not mute_users:
                print(f"{self.SRC} is empty.")
                return
        for line in mute_users:
            if not line:
                continue
            if line.startswith("#"): # コメント行は無視
                continue
            if line.startswith("!"): # フィルター側のコメントがでたらそこまでのユーザーを追加する
                if users:
                    user_list = ",".join(self.USER_BASE.format(name=user) for user in users)
                    filters_lines.append(self.FILTER_BASE.format(users=user_list))
                filters_lines.append(line)
                users = [] # ユーザーリストをリセット
                continue
            if line.startswith("@"): # ユーザー名の行
                users.append(line[1:]) # @を除去してユーザー名を追加
        # 残されたユーザーを追加
        if users:
            user_list = ",".join(self.USER_BASE.format(name=user) for user in users)
            filters_lines.append(self.FILTER_BASE.format(users=user_list))
        # ファイルに書き込む
        with open(self.DIST, "w", encoding="utf-8") as f:
            f.write("\n".join(filters_lines) + "\n")
