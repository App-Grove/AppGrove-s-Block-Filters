# main.py

# 必要なライブラリをインポート
from pathlib import Path

# スクリプトをインポート
from Twitter.generate_bad_urls import GenerateBadUrls
from Twitter.generate_mute_users import GenerateMuteUsers
from Twitter.generate_mute_words import GenerateMuteWords

# パスを取得
REPO_ROOT = Path(__file__).resolve().parent.parent

def main():
    generate_bad_urls = GenerateBadUrls(REPO_ROOT)
    generate_bad_urls.run()

    generate_mute_users = GenerateMuteUsers(REPO_ROOT)
    generate_mute_users.run()

    generate_mute_words = GenerateMuteWords(REPO_ROOT)
    generate_mute_words.run()

if __name__ == "__main__":
    main()
