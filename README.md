# isaac_min_ws

Reproducible ROS2 workspace for Isaac ROS Visual SLAM with RealSense camera.

## ビルド時のトラブルシューティング

### magic_enum エラーの修正方法

`isaac_ros_nitros_image_type`ビルド時に`magic_enum was not declared`エラーが出る場合：

```bash
# ビルド後、インストールされたヘッダーファイルを編集
nano ~/isaac_min_ws/install/share/isaac_ros_gxf/gxf/include/gxf/core/expected_macro.hpp
```

84行目付近の`magic_enum::enum_name`部分を確認し、必要に応じて修正してください。

**注意**: `src/_global_include/magic_enum_shim.hpp`が環境で正しく設定されている必要があります。

## ROS_DOMAIN_ID設定について

ネットワーク経由で通信する場合、JetsonとSurface（WSL）で同じROS_DOMAIN_IDを設定してください。

### Jetson側での起動

```bash
# 環境変数を設定（例：ID 42を使用）
export ROS_DOMAIN_ID=42

# vslam_bringupを起動
```

### Surface（WSL側）での設定

```bash
# 同じROS_DOMAIN_IDを設定
export ROS_DOMAIN_ID=42
```

これにより、Jetsonで実行中のVSLAMのトピックがSurface側からアクセス可能になります。

## パッケージ構成

- `vslam_bringup`: RealSense + Isaac ROS Visual SLAM の起動設定
- `perception_vslam`: VSLAM基本設定
- `warehouse_mapper`: 倉庫マッピング機能（開発中）
