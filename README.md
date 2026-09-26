# AppGrove's Block Filters

AppGroveが管理する[uBlock Origin](https://github.com/gorhill/uBlock)のブロックリストです。

基本的にEasy ListとuBlock Filtersを使用するため広告ブロック用フィルターは作成しないと思います。  
また、偽サイトについても[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)を使用しているため対応しません。

## 使い方

1. uBlock Originをインストールする
2. 下の「フィルターリスト」から使いたいフィルターを選ぶ
3. 「インストール」リンクを開く
4. uBlock Originが自動で認識し、内容の確認画面とともに「購読」ボタンが表示されるので、クリックする

### uBlock Originのインストール
- FireFox系ブラウザ: [uBlock Origin - Add-ons for Firefox](https://addons.mozilla.org/ja/firefox/addon/ublock-origin/)
- Edge: [uBlock Origin - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/ublock-origin/odfafepnkmbhccpbejgmiehpchacaeak)
- Opera: [uBlock Origin - Opera add-ons](https://addons.opera.com/ja/extensions/details/ublock/)
- 手動インストール: [uBlock Origin - GitHub](https://github.com/gorhill/uBlock)

Google Chromeでは、uBlock Originが必要とするManifest V2がサポートされなくなったため、uBlock Originをインストールできません。Vivaldi等のChromium系ブラウザでも将来的に同様の状況になる可能性があります。  
以前まではChromeウェブストアからuBlock Originをインストールできましたが、2026年8月をもってGoogleはManifest V2拡張機能をストアから削除しました。現在、独自のストアを持たずChromeウェブストアに依存するChromiumブラウザでuBlock Originをインストールするには、GitHubから手動でインストールする必要があります。
  
#### Androidの場合
Androidで拡張機能をサポートしたブラウザはあまり多くありません。FireFox系ブラウザであればほとんどの場合拡張機能をサポートしていますが、個人的には以下のChromium系ブラウザを推奨します:
- [Titanium Browser](https://play.google.com/store/apps/details?id=io.github.jqssun.helium)
- [Bare Browser](https://github.com/BareBrowser/bare-browser)

Titanium BrowserはManifest V2をサポートしており、uBlock Originをインストールできます。Playストアから更新できます。  
Bare BrowserはManifest V2をサポートしており、uBlock Originが組み込まれています。ストアにないためObtanium等を使用してGitHubからインストールしてください。

Bare Browserの紹介記事: https://note.com/daizu_lab/n/nc20fecb20159

### uBlock Origin liteでの使い方
※ 十分にテストしていません。動作報告や手順の更新を歓迎します。

#### 1. uBlock Origin liteのインストール
- Chrome/Titanium等: [uBlock Origin Lite - Chrome ウェブストア](https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh)
- Edge: [uBlock Origin Lite - Microsoft Edge Addons](https://microsoftedge.microsoft.com/addons/detail/ublock-origin-lite/cimighlppcgcoapaliogpjjdehbnofhn)
- Safari: [uBlock Origin Lite - App Store](https://apps.apple.com/us/app/ublock-origin-lite/id6745342698)
- 手動インストール: [uBlock Origin Lite - GitHub](https://github.com/uBlockOrigin/uBOL-home)

※※工事中※※

## フィルターリスト

### Twitter

#### daizu's twitter mute words

Twitterで不快なポストを非表示にするためのフィルターです。アカウントに関わらず、また抜け漏れなく、検索結果も含めてブロックします。  
このフィルターは、Twitterの投稿から受けるストレスの軽減を目指しているもので、言葉狩りや表現規制に賛同するものではなく、むしろ自衛を容易にすることで表現の自由の保護につながると考えています。
一部のスパム投稿に使われやすいドメインを含む投稿もブロック対象としています。見つけ次第追加しますが、抜け漏れを見かけた場合は[issue](https://github.com/App-Grove/AppGrove-s-Block-Filters/issues)から報告してください。目的が異なるためフィルターの分離も検討しています。また、Twitterでの投稿非表示のみを対象にしているため、実際のアクセスをブロックしたい場合は、[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)等のフィルターを使用してください。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FTwitter%2Fmute_words.txt\&title=daizu%27s%20twitter%20mute%20words)

```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/mute_words.txt
```

#### I don't need old news on Twitter

Twitterで古いニュースを非表示にします。現在は、Gigazineの過去記事再投稿(投稿の最後に投稿年が書かれた投稿)のみが対象です。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FTwitter%2Fold_news.txt\&title=I%20don%27t%20need%20old%20news%20on%20Twitter)

```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/old_news.txt
```

#### daizu's twitter mute users

一部のTwitterユーザーの投稿を非表示にします。独断と偏見でストレスの原因になりやすそうなユーザーを選びました。  
対象ユーザーの主張に賛同/反対するものではなく、また当人を攻撃する意思もありません。当人に全く非がない場合でも、周囲の反応等でストレスになる可能性があると判断した場合はブロック対象にしています。  
issueやDM等で連絡をくださればブロック対象から外す等の対応も可能です。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FTwitter%2Fmute_users.txt\&title=daizu%27s%20twitter%20mute%20users)

```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/mute_users.txt
```

### YouTube

#### YouTube End Screen

YouTube動画の最後に表示されるオーバーレイコンテンツを可能な限り非表示にするためのフィルターです。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FYouTube%2Fend_screen.txt\&title=Hide%20YouTube%20End%20Screen%20Contents)

```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/YouTube/end_screen.txt
```

#### Don't ask me about YouTube Premium

YouTubeにまれに表示されるYouTube Premiumの機能について尋ねる謎のアンケートを非表示にします。
すでに購読されている方のためにフィルターは残しますが、fanboy_annoyance_specific_hide.txtに含まれているため、そちらの購読をおすすめします。YouTube Premiumアンケートの非表示のみを行いたい場合は、こちらのフィルターを購読してください。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FYouTube%2Fpremium_survey.txt\&title=Don%27t%20ask%20me%20about%20YouTube%20Premium)

```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/YouTube/premium_survey.txt
```

### Bing

#### I don't have questions for Copilot while searching on Bing

Bing検索の株に表示されるCopilotの質問欄を非表示にするためのフィルターです。

[インストール](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FApp-Grove%2FAppGrove-s-Block-Filters%2Frefs%2Fheads%2Fmain%2FBing%2Fcopilot_followup.txt\&title=I%20don%27t%20have%20questions%20for%20Copilot%20while%20searching%20on%20Bing)
```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Bing/copilot_followup.txt
```

## 一括インストール
このリポジトリに含まれるすべてのフィルターを一括でインストールしたい場合は以下のリンク集をコピペしてください。
```
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/mute_words.txt
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/old_news.txt
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Twitter/mute_users.txt
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/YouTube/end_screen.txt
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/YouTube/premium_survey.txt
https://raw.githubusercontent.com/App-Grove/AppGrove-s-Block-Filters/refs/heads/main/Bing/copilot_followup.txt
```

## ライセンス
このリポジトリで提供されるフィルターリストは、特に断りがない限り、Apache License 2.0の下でライセンスされています。詳細は[LICENSE](LICENSE)をご覧ください。

ただし、以下のフィルターリストは、別のライセンスで提供されています。詳細は各ファイルの先頭に記載されています。
- [Don't ask me about YouTube Premium](YouTube/premium_survey.txt): [GPL-3.0-or-later](LICENSE-GPL-3.0-or-later.txt)

## クレジット
このフィルターリストの作成にあたって、以下を参考にさせていただきました。
- [uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin) by [Kdroidwin](https://github.com/Kdroidwin): uBlockOrigin向けリストの基本形を参考にしました
- [gist:488dac5770c2a3cc36edc9139b625190](https://gist.github.com/Yuki2718/488dac5770c2a3cc36edc9139b625190) by [Yuki2718](https://github.com/Yuki2718): Twitterで特定ユーザーの投稿を非表示にする方法を参考にしました  
- [fanboy_annoyance_specific_hide.txt](https://github.com/easylist/easylist/blob/master/fanboy-addon/fanboy_annoyance_specific_hide.txt): YouTube Premiumのアンケートを非表示にする方法を参考にしました
  
このフィルターの作成に協力してくださったすべての方に感謝を申し上げます。以下に、主な貢献者の主な貢献内容を記載します。
- [Kdroidwin](https://github.com/Kdroidwin)
  - [直接インストールできるリンクの追加](https://github.com/App-Grove/AppGrove-s-Block-Filters/pull/1)
  - [Twitter向けミュートワードの追加](https://github.com/App-Grove/AppGrove-s-Block-Filters/pull/1)
- [Yuki2718](https://github.com/Yuki2718)
  - [uBlock Originで特定ユーザーの投稿を非表示にする方法の提供](https://x.com/Yuki27183/status/2082784790269534284?s=20)
