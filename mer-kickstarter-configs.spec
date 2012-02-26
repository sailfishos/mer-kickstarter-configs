Name:       mer-kickstarter-configs
Summary:    Kickstarter configs for Mer Core
Version:    0.2
Release:    1
Group:      System/Base
License:    Public Domain
BuildArch:  noarch
URL:        http://www.merproject.org
Source0:    00base.yaml
Source1:    00reference.yaml
Source2:    Makefile
Source3:    rpm-rebuilddb.post
Source4:    prelink.post
Source5:    qmlviewer-session.post
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Create Configuration files to build Mer Core products with

%prep
%setup -q -c -n %{name}-%{version} -T
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/kickstarter-configs/mer/00base.yaml
%{_datadir}/kickstarter-configs/mer/rpm-rebuilddb.post
%{_datadir}/kickstarter-configs/mer/prelink.post
%{_datadir}/kickstarter-configs/mer-reference-images/00reference.yaml
%{_datadir}/kickstarter-configs/mer-reference-images/qmlviewer-session.post

# << files
