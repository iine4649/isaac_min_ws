# isaac_min_ws

Reproducible ROS2 workspace for Isaac ROS Visual SLAM with RealSense camera.

## ROS_DOMAIN_ID設定について

ネットワーク経由で通信する場合、JetsonとSurface（WSL）で同じROS_DOMAIN_IDを設定してください。

### Jetson側での起動

```bash
# 環境変数を設定（例：ID 42を使用）
export ROS_DOMAIN_ID=42

# vslam_bringupを起動
ros2 launch vslam_bringup bringup_min.launch.py
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
