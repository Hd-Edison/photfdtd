from photfdtd.fdtd.constants import c
# pulse_oscillation(frequency=, t=, pulselength=, offset=)

# pulselength = 6.49946e-15

# bandwidth = 0.44 / (pulselength)
# print("bandwidth = %f THz" % (bandwidth * 1e-12))
# print("bandwidth = %f um" % (bandwidth * wavelength ** 2 / c * 1e6))


def calculate_pulselength_or_bandwidth(pulselength=None, bandwidth=None, wl_unit: bool = False):
    """
    计算脉宽或带宽。

    :param pulselength: 脉宽，单位为秒 (可选)
    :param bandwidth: 带宽，单位为Hz (可选)
    :return: 如果提供的是脉宽，返回带宽；如果提供的是带宽，返回脉宽。
    :raises ValueError: 如果既未提供脉宽又未提供带宽，或提供了两个参数，则引发异常。
    """
    if pulselength is not None and bandwidth is not None:
        raise ValueError("只能提供一个参数：脉宽或带宽。")

    if pulselength is not None:
        bandwidth = 0.44 / pulselength
        print(f"bandwidth = {bandwidth * 1e-12} THz, {bandwidth * wavelength ** 2 / c * 1e6} um")
        return

    if bandwidth is not None:
        if wl_unit:
            # um单位
            bandwidth = bandwidth * c / (wavelength ** 2)
        pulselength = 0.44 / bandwidth
        print("pulselength = %f fs" % (pulselength * 1e15))


wavelength = 1550e-9 # m
print("center wavelength = %f um" % (wavelength * 1e6))
try:
    calculate_pulselength_or_bandwidth(pulselength=4.4e-15)  # 输入脉宽 s
    calculate_pulselength_or_bandwidth(bandwidth=100e-9, wl_unit=True)  # 输入带宽为 THz
except ValueError as e:
    print(e)
