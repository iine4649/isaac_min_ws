export PATH=/usr/bin:/bin:/usr/local/bin
source /opt/ros/humble/setup.bash
export HOME=/home/xkura
export CUDA_HOME=/usr/local/cuda
export CUDACXX=/usr/local/cuda/bin/nvcc
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export ISAAC_CXX_FLAGS="-std=gnu++17 -isystem /opt/ros/humble/include -isystem /opt/ros/humble/include/foxglove_msgs -I/home/xkura/isaac_min_ws/src/_global_include -include magic_enum_shim.hpp"
