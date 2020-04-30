# Perfume AI

Perfume メンバーの画像をアップロードすると、AI が

- のっち
- あーちゃん
- かしゆか

を識別してくれる AI アプリです。

## セットアップ

```bash
# install dependencies
$ yarn install

# serve with hot reload at localhost:3000
$ yarn dev

# generate static project
$ yarn generate
```

## API Server

api フォルダにコード一式を載せています。

- POST された base64 形式のデータをデコード
- 学習済みモデルで推論
- 切り取った顔を base64 形式にエンコード
- 推論結果と base64 形式のデータをフロントへレスポンス

## Perfume AI model script

`api/deep_learning/main` に、Perfume AI の学習済みモデルを作るコードを載せています。

### 実行環境

- Google Colaboratory
- PyTorch：1.4.0
- PyTorch Lightning：0.7.4

画像データは各自、用意して下さい。
