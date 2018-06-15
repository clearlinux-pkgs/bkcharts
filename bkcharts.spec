#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bkcharts
Version  : 0.2
Release  : 12
URL      : http://pypi.debian.net/bkcharts/bkcharts-0.2.tar.gz
Source0  : http://pypi.debian.net/bkcharts/bkcharts-0.2.tar.gz
Summary  : High level chart types built on top of Bokeh
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bkcharts-python3
Requires: bkcharts-python
Requires: numpy
Requires: six
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the bkcharts package.
Group: Default
Requires: bkcharts-python3

%description python
python components for the bkcharts package.


%package python3
Summary: python3 components for the bkcharts package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bkcharts package.


%prep
%setup -q -n bkcharts-0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523286259
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
