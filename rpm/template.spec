%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-mvsim
Version:        0.9.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mvsim package

License:        BSD
URL:            https://wiki.ros.org/mvsim
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       cppzmq-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       pybind11-devel
Requires:       python3-libs
Requires:       python3-pip
Requires:       python3-protobuf
Requires:       ros-rolling-mrpt2
Requires:       ros-rolling-nav-msgs
Requires:       ros-rolling-ros2launch
Requires:       ros-rolling-sensor-msgs
Requires:       ros-rolling-tf2
Requires:       ros-rolling-tf2-geometry-msgs
Requires:       ros-rolling-visualization-msgs
Requires:       unzip
Requires:       wget
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  cmake3
BuildRequires:  cppzmq-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-libs
BuildRequires:  python3-pip
BuildRequires:  python3-protobuf
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-cmake-xmllint
BuildRequires:  ros-rolling-mrpt2
BuildRequires:  ros-rolling-nav-msgs
BuildRequires:  ros-rolling-ros-environment
BuildRequires:  ros-rolling-sensor-msgs
BuildRequires:  ros-rolling-tf2
BuildRequires:  ros-rolling-tf2-geometry-msgs
BuildRequires:  ros-rolling-visualization-msgs
BuildRequires:  unzip
BuildRequires:  wget
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
%endif

%description
A lightweight multivehicle simulation framework.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Mar 21 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.9.2-1
- Autogenerated by Bloom

* Thu Mar 14 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.9.1-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Jose-Luis Blanco-Claraco <jlblanco@ual.es> - 0.8.3-2
- Autogenerated by Bloom

