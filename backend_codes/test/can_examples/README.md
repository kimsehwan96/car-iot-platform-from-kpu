## PYTHON-CAN 모둘 사용법 및 시뮬레이션

### 가상머신 이용(Linux, ubuntu)
- Virtual Can interfadce를 이용해서 사용 가능하다.

```console
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

- 이렇게 하면 virtual socket can 사용 가능하다.
    - 우리는 socketcan 이용 할 예정임.
